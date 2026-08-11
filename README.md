# Repo Sense

Repo Sense is a self-contained prompt validation and evaluation framework aimed at helping teams manage, test, and harden LLM prompts and guardrails. It provides:

- Static prompt validation (schema and rule checks)
- A DAST-style ephemeral evaluation harness that spins up an isolated Ollama container for dynamic testing
- Architecture-level checks (repository hygiene rules enforced as tests)
- A lightweight, reproducible test / CI workflow

This repository is designed to run in CI or locally with minimal setup. The project uses `uv` as the build/test driver and pins Python to the 3.11.x series.

Quick links
- Project metadata: [pyproject.toml](pyproject.toml)
- Python version helper: [.python-version](.python-version)
- Build & test driver: [Makefile](Makefile)
- Validation docs: [abilities/validation/README.md](abilities/validation/README.md)
- Contribution guide: [CONTRIBUTING.md](CONTRIBUTING.md)
- CI workflow: [.github/workflows/ci.yml](.github/workflows/ci.yml)

Quickstart (local)

1. Create and activate a virtual environment matching the pinned Python:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
```

2. Install the package in editable mode and required test tools:

```bash
pip install -e .
pip install pytest httpx
# Integration test requirements (only needed to run integration suite):
pip install testcontainers docker
```

3. Run the default test target (unit + architecture checks):

```bash
make unit
```

4. Run integration tests (requires Docker and access to the Docker socket):

```bash
make integration
```

Testing layout
- Unit tests: `abilities/validation/tests/unit/` — fast, no external services required.
- Architecture tests: `abilities/validation/tests/architecture/` — repository-level rules (no prints, no bare except, no TODO/FIXME, no obvious hardcoded secrets).
- Integration tests: `abilities/validation/tests/integration/` — ephemeral Ollama container + dynamic prompt evaluations. These tests may pull models on first run and require Docker access.

Evaluation harness
The self-contained prompt evaluation harness and cases live under `abilities/validation/evals/`. Example cases are at [abilities/validation/evals/cases.yaml](abilities/validation/evals/cases.yaml) and are exercised by the integration tests.

Docker & CI notes
- Integration tests use Testcontainers to manage the Ollama container. CI runners must allow creating Docker containers.
- If running in nested CI or a privileged environment, grant access to the host Docker daemon by mounting the Docker socket into the runner:

```bash
# Example: when running a containerized CI job, mount the host docker socket
docker run -v /var/run/docker.sock:/var/run/docker.sock ...
```

- If Docker socket mounting is not permitted, provide a separate service (sibling Docker host) or use privileged runners with Docker-in-Docker support.

Continuous Integration
The repository includes a GitHub Actions workflow at [.github/workflows/ci.yml](.github/workflows/ci.yml) that runs unit/architecture tests on push/PR against `main` and then runs integration tests (when runners allow Docker).

Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines and test expectations.

Questions or issues
If you hit environment issues (Python version mismatch, missing `uv` module, Docker access), please share the failing command and output — the Makefile and this README aim to make the expected commands explicit and reproducible.
