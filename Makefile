PYTHON_VERSION ?= 3.11
UV := uv

.PHONY: help install test validate build clean unit integration arch lint

help:
	@echo "Repo Sense Makefile commands:"
	@echo "  make install        Install project dependencies using uv"
	@echo "  make test           Run pytest for static validation"
	@echo "  make validate       Run prompt validation (alias for test)"
	@echo "  make build          Build the package using uv"
	@echo "  make clean          Remove Python build artifacts"
	@echo "  make lint           Run linting if configured"

install:
	@echo "Syncing dependencies with uv..."
	$(UV) pip compile pyproject.toml -o requirements.txt --python $(PYTHON_VERSION)
	$(UV) pip sync requirements.txt --python $(PYTHON_VERSION)

test: unit

unit:
	@echo "Running unit + architecture tests via uv"
	$(UV) run --python $(PYTHON_VERSION) pytest tests/validation/unit tests/validation/architecture

arch:
	@echo "Running architecture tests via uv"
	$(UV) run --python $(PYTHON_VERSION) pytest tests/validation/architecture

integration:
	@echo "Running integration tests via uv"
	$(UV) run --python $(PYTHON_VERSION) pytest tests/validation/integration

validate: test

build:
	@echo "Building distribution packages using uv"
	$(UV) build --python $(PYTHON_VERSION)

clean:
	rm -rf dist build *.egg-info .pytest_cache requirements.txt .venv
	find . -name "__pycache__" -type d -prune -exec rm -rf '{}' +
