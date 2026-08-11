from pathlib import Path
import re


def test_no_hardcoded_secrets():
    base = Path(__file__).resolve().parents[3]
    violations = []
    secret_patterns = [re.compile(r"(?i)(secret|password|api_key|token)\s*=\s*['\"]([A-Za-z0-9_\-]{8,})['\"]")]
    for p in base.rglob("*.py"):
        if "abilities/validation/tests" in str(p):
            continue
        text = p.read_text(encoding="utf-8")
        for pat in secret_patterns:
            if pat.search(text):
                violations.append(f"Possible hardcoded secret in {p}")
    assert not violations, "Hardcoded secrets detected:\n" + "\n".join(violations)
