# Ability Prompt Validation

This folder contains validation artifacts and test fixtures for prompt assets stored in `abilities/prompts/`.

## Purpose

* Define how prompt files in `abilities/prompts/` are validated.
* Keep example prompt fixtures for guardrail and schema tests.
* Record evaluation workflows for prompt quality checks.

## Validation contents

* `prompt-metadata.schema.yaml` - schema file for prompt metadata.
* `rules/guardrails.yaml` - structured static validation rules driven by guardrails.
* `tests/` - pytest cases for prompt schema and guardrail validation.
* `fixtures/` - optional example prompt files used for validation.
* `evals/` - evaluation definitions if using a prompt evaluation framework.
	This folder now contains a self-contained Python evaluation harness that does not
	require external `promptfoo` installation. Tests spin up an isolated Ollama
	container and run the evaluation cases in `evals/cases.yaml`.

## Guardrails location

Prompt guardrails are stored in `abilities/prompts/guardrails.md` and enforced by the YAML rules in `abilities/validation/rules/guardrails.yaml`.

Prompt guardrails are stored in `abilities/prompts/guardrails.md`.
