PYTHON ?= python3.11
PIP := $(PYTHON) -m pip
# Run uv via the selected Python interpreter to ensure uv executes under the pinned Python
UV := $(PYTHON) -m uv

.PHONY: help install test validate build clean unit integration arch

help:
	@echo "Repo Sense Makefile commands:"
	@echo "  make install        Install project dependencies"
	@echo "  make test           Run pytest for static validation"
	@echo "  make validate       Run prompt validation (alias for test)"
	@echo "  make build          Build the package using uv"
	@echo "  make clean          Remove Python build artifacts"
	@echo "  make lint           Run linting if configured"

install:
	$(PIP) install --upgrade pip
	$(PIP) install .

test: unit

unit:
	@echo "Running unit + architecture tests"
	-@$(PYTHON) -m uv run pytest abilities/validation/tests/unit abilities/validation/tests/architecture || uv run pytest abilities/validation/tests/unit abilities/validation/tests/architecture

arch:
	@echo "Running architecture tests"
	-@$(PYTHON) -m uv run pytest abilities/validation/tests/architecture || uv run pytest abilities/validation/tests/architecture

integration:
	@echo "Running integration tests"
	-@$(PYTHON) -m uv run pytest abilities/validation/tests/integration || uv run pytest abilities/validation/tests/integration

validate: test

build:
	@echo "Building using $(PYTHON) -m uv if available, else falling back to uv binary"
	-@$(PYTHON) -m uv build . || uv build .

clean:
	rm -rf dist build *.egg-info .pytest_cache
	find . -name "__pycache__" -type d -prune -exec rm -rf '{}' +
