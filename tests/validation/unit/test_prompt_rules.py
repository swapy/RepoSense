import glob
import os
import re
import yaml
from pathlib import Path

# Resolve project root (where pyproject.toml lives) so tests work from nested test dirs
def find_project_root() -> str:
    p = Path(__file__).resolve()
    for parent in p.parents:
        if (parent / "pyproject.toml").exists():
            return str(parent)
    # fallback: ascend 4 levels (sensible default)
    return str(p.parents[4])

BASE_DIR = find_project_root()
RULES_PATH = os.path.join(BASE_DIR, "abilities", "validation", "rules", "guardrails.yaml")
PROMPT_DIR = os.path.join(BASE_DIR, "abilities", "prompts")

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def get_prompt_files():
    pattern = os.path.join(PROMPT_DIR, "**", "*.yaml")
    return glob.glob(pattern, recursive=True)

def load_prompt(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def test_rule_config_exists():
    assert os.path.exists(RULES_PATH), f"Guardrail rule config not found: {RULES_PATH}"

def test_prompt_body_length():
    rules = load_yaml(RULES_PATH)
    min_length = rules.get("minimum_prompt_length", 0)
    for prompt_path in get_prompt_files():
        prompt = load_prompt(prompt_path)
        prompt_text = prompt.get("prompt", "")
        assert len(prompt_text.strip()) >= min_length, f"Prompt too short in {prompt_path}: {len(prompt_text.strip())} characters"

def test_forbidden_phrases_in_prompt():
    rules = load_yaml(RULES_PATH)
    patterns = rules.get("forbidden_phrases", [])
    for prompt_path in get_prompt_files():
        prompt = load_prompt(prompt_path)
        prompt_text = prompt.get("prompt", "")
        for phrase in patterns:
            assert phrase.lower() not in prompt_text.lower(), f"Forbidden phrase '{phrase}' found in {prompt_path}"

def test_sensitive_terms_in_prompt():
    rules = load_yaml(RULES_PATH)
    terms = rules.get("sensitive_terms", [])
    for prompt_path in get_prompt_files():
        prompt = load_prompt(prompt_path)
        prompt_text = prompt.get("prompt", "")
        for term in terms:
            assert term.lower() not in prompt_text.lower(), f"Sensitive term '{term}' found in {prompt_path}"

def test_broad_scope_phrases_in_prompt():
    rules = load_yaml(RULES_PATH)
    phrases = rules.get("broad_scope_phrases", [])
    for prompt_path in get_prompt_files():
        prompt = load_prompt(prompt_path)
        prompt_text = prompt.get("prompt", "")
        for phrase in phrases:
            assert phrase.lower() not in prompt_text.lower(), f"Broad scope phrase '{phrase}' found in {prompt_path}"

def test_placeholder_patterns_in_prompt():
    rules = load_yaml(RULES_PATH)
    patterns = rules.get("placeholder_patterns", [])
    for prompt_path in get_prompt_files():
        prompt = load_prompt(prompt_path)
        prompt_text = prompt.get("prompt", "")
        for pattern in patterns:
            assert not re.search(pattern, prompt_text), f"Placeholder pattern '{pattern}' found in {prompt_path}"

def test_prompt_evidence_language():
    rules = load_yaml(RULES_PATH)
    indicators = rules.get("evidence_indicators", [])
    for prompt_path in get_prompt_files():
        prompt = load_prompt(prompt_path)
        prompt_text = prompt.get("prompt", "")
        assert any(indicator.lower() in prompt_text.lower() for indicator in indicators), (
            f"Prompt in {prompt_path} does not mention evidence or output indicators"
        )