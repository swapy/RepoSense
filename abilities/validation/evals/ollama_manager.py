import asyncio
from pathlib import Path
from typing import Tuple

import httpx
from testcontainers.core.container import DockerContainer

OLLAMA_IMAGE = "ollama/ollama:latest"
OLLAMA_API_PORT = 11434


def ensure_cache_directory(cache_dir: Path) -> None:
    cache_dir.mkdir(parents=True, exist_ok=True)


async def wait_for_http_service(host: str, port: int, timeout_seconds: int = 30) -> None:
    deadline = asyncio.get_event_loop().time() + timeout_seconds
    url = f"http://{host}:{port}/"
    async with httpx.AsyncClient(timeout=3.0) as client:
        while True:
            if asyncio.get_event_loop().time() > deadline:
                raise TimeoutError(f"Service did not become available at {url} within {timeout_seconds}s")
            try:
                r = await client.get(url)
                if r.status_code < 500:
                    return
            except (httpx.TransportError, httpx.ConnectError, httpx.ReadTimeout):
                pass
            await asyncio.sleep(0.5)


class OllamaContainer:
    def __init__(self, model: str, host_cache: Path | None = None):
        self.model = model
        self.host_cache = host_cache or (Path.home() / ".ollama")
        self.container: DockerContainer | None = None
        self.host: str | None = None
        self.port: int | None = None

    async def start(self) -> Tuple[str, int]:
        ensure_cache_directory(self.host_cache)
        cmd = ["sh", "-c", f"ollama pull {self.model} && ollama serve --listen 0.0.0.0:{OLLAMA_API_PORT}"]

        container = DockerContainer(OLLAMA_IMAGE)
        container.with_bind_mount(str(self.host_cache), "/root/.ollama")
        container.with_exposed_ports(OLLAMA_API_PORT)
        container.with_command(cmd)

        await asyncio.to_thread(container.start)
        self.container = container
        self.host = await asyncio.to_thread(container.get_container_host_ip)
        self.port = int(await asyncio.to_thread(container.get_exposed_port, OLLAMA_API_PORT))

        await wait_for_http_service(self.host, self.port)
        return self.host, self.port

    async def stop(self) -> None:
        if self.container:
            await asyncio.to_thread(self.container.stop)
            self.container = None