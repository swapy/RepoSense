from pathlib import Path
import re


def test_no_bare_except_blocks():
    base = Path(__file__).resolve().parents[3]
    violations = []
    pattern = re.compile(r"^\s*except\s*:\s*(#.*)?$", re.MULTILINE)
    for p in base.rglob("*.py"):
        if "abilities/validation/tests" in str(p):
            continue
        text = p.read_text(encoding="utf-8")
        if pattern.search(text):
            violations.append(f"bare except found in {p}")
    assert not violations, "Bare except blocks detected:\n" + "\n".join(violations)
