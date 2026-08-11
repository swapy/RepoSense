import glob
import os
import yaml
from jsonschema import Draft202012Validator

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SCHEMA_PATH = os.path.join(BASE_DIR, "abilities", "schemas", "prompt-metadata.schema.yaml")
PROMPT_DIR = os.path.join(BASE_DIR, "abilities", "prompts")


def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_prompt_files():
    pattern = os.path.join(PROMPT_DIR, "**", "*.yaml")
    return glob.glob(pattern, recursive=True)


def test_prompt_metadata_schema_exists():
    assert os.path.exists(SCHEMA_PATH), f"Schema file not found: {SCHEMA_PATH}"


def test_all_prompt_metadata_validate_against_schema():
    schema = load_yaml(SCHEMA_PATH)
    validator = Draft202012Validator(schema)

    errors = []
    for prompt_path in get_prompt_files():
        prompt = load_yaml(prompt_path)
        for error in validator.iter_errors(prompt):
            errors.append((prompt_path, error.message))

    assert not errors, "Schema validation failed:\n" + "\n".join(f"{path}: {message}" for path, message in errors)
