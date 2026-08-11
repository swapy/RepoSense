import glob
import os
import re
import yaml

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
PROMPT_DIR = os.path.join(BASE_DIR, "abilities", "prompts")

FORBIDDEN_PATTERNS = [
    r"\bmodify repository code\b",
    r"\bpatch repository code\b",
    r"\bgenerate code\b",
    r"\bchange the code\b",
    r"\bapply the patch\b",
    r"\bcommit the changes\b",
]


def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_prompt_files():
    pattern = os.path.join(PROMPT_DIR, "**", "*.yaml")
    return glob.glob(pattern, recursive=True)


def test_all_prompts_have_prompt_body():
    for prompt_path in get_prompt_files():
        prompt = load_yaml(prompt_path)
        assert "prompt" in prompt and isinstance(prompt["prompt"], str) and prompt["prompt"].strip(), f"Missing or empty prompt body in {prompt_path}"


def test_forbidden_prompt_language():
    for prompt_path in get_prompt_files():
        prompt = load_yaml(prompt_path)
        prompt_text = prompt.get("prompt", "")
        for pattern in FORBIDDEN_PATTERNS:
            assert not re.search(pattern, prompt_text, re.IGNORECASE), f"Forbidden prompt language in {prompt_path}: {pattern}"
