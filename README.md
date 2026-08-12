# Repo Sense — Software Assessment Framework

Repo Sense is a repository assessment framework that uses prompt-driven automation and guardrails to evaluate software projects. It combines static validation rules, repository-level architecture checks, and LLM-assisted analysis (used as an assistant, not the target) to produce evidence-based findings about code quality, security, and maintainability.

Tagline

"Automated repository assessments driven by prompts and guardrails — evidence-first, LLM-assisted checks."

Key capabilities

- Static prompt and metadata validation (schema and rule checks)
- Repository architecture tests enforcing hygiene and policy (no print(), no bare except, no hardcoded secrets, etc.)
- Integration evaluation harness that runs controlled LLM-assisted analyses when needed
- CI-ready workflows and reproducible environments (Python 3.11.x, `uv` build driver)

Suggested repository topics/tags

- `software-assessment`
- `repo-audit`
- `prompt-engineering`
- `llm-assisted`
- `guardrails`
- `testing`
- `ci`
- `security`

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
pip install pytest httpx pytest-asyncio
# Integration test requirements (only needed to run integration suite):
pip install testcontainers docker
```

3. Run the default unit + architecture tests:

```bash
make unit
```

4. Run integration tests (requires Docker and access to the Docker socket):

```bash
make integration
```

Testing layout

- Unit tests: `tests/validation/unit/` — fast, no external services required.
- Architecture tests: `tests/validation/architecture/` — repository-level rules enforced as tests.
- Integration tests: `tests/validation/integration/` — optional, LLM-assisted analyses that may pull models and require Docker.

Evaluation harness

The self-contained evaluation harness and cases live under `src/abilities/validation/evals/` and test fixtures are stored under `tests/fixtures/evals/`. Example cases are at [tests/fixtures/evals/cases.yaml](tests/fixtures/evals/cases.yaml) and are exercised by the integration tests when enabled.

Docker & CI notes

- Integration tests use Testcontainers to manage ephemeral evaluation services. CI runners must allow creating Docker containers or provide an alternate host Docker service.
- If running in nested CI or a privileged environment, grant access to the host Docker daemon by mounting the Docker socket into the runner:

```bash
# Example: when running a containerized CI job, mount the host docker socket
docker run -v /var/run/docker.sock:/var/run/docker.sock ...
```

Continuous Integration

The repository includes a GitHub Actions workflow at [.github/workflows/ci.yml](.github/workflows/ci.yml) that runs unit/architecture tests on push/PR against `main` and then runs integration tests (when runners allow Docker).

Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines and test expectations.

If you hit environment issues (Python version mismatch, missing `uv` module, Docker access), please share the failing command and output — the Makefile and this README aim to make the expected commands explicit and reproducible.
