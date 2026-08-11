import asyncio
import yaml
from pathlib import Path
import sys

# Ensure repository root is on sys.path so local `abilities` package imports work
repo_root = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(repo_root))

import pytest

from abilities.validation.evals.ollama_manager import OllamaContainer
from abilities.validation.evals.harness import run_cases

MODEL = "qwen2.5:0.5b"


def load_cases(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


@pytest.mark.asyncio
async def test_prompt_evaluation_harness():
    cases_path = Path(__file__).resolve().parents[1] / "evals" / "cases.yaml"
    cases = load_cases(cases_path)

    container = OllamaContainer(MODEL)
    try:
        host, port = await container.start()
        results = await run_cases(host, port, MODEL, cases)

        failures = [r for r in results if not r["result"]["passed"]]
        assert not failures, f"Evaluation failures: {failures}"
    finally:
        await container.stop()
