# Contributing

Thank you for contributing to Repo Sense. Suggestions, fixes, and tests are welcome.

Guidelines:

- Run unit and architecture tests before opening a PR: `make test`.
- Run integration tests locally if you change evaluation or DAST code. Integration tests require Docker and may pull models.
- Follow the project's Python version: see `.python-version` (Python 3.11).
- Avoid committing secrets or large model artifacts.
- Keep changes focused and add tests for new behavior.

If you're adding an evaluation case, place it under `abilities/validation/evals/` and document it in `abilities/validation/README.md`.
