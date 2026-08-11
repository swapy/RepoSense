from pathlib import Path


def test_no_todo_comments():
    base = Path(__file__).resolve().parents[3]
    violations = []
    for p in base.rglob("*.py"):
        if "abilities/validation/tests" in str(p):
            continue
        text = p.read_text(encoding="utf-8")
        if "TODO" in text or "FIXME" in text:
            violations.append(f"TODO/FIXME found in {p}")
    assert not violations, "TODO/FIXME comments present:\n" + "\n".join(violations)
