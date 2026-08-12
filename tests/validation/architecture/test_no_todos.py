from pathlib import Path


def test_no_todo_comments():
    repo_root = Path(__file__).resolve()
    while repo_root != repo_root.parent and not (repo_root / "pyproject.toml").exists():
        repo_root = repo_root.parent
    violations = []
    for p in repo_root.rglob("*.py"):
        if "tests/validation" in str(p):
            continue
        text = p.read_text(encoding="utf-8")
        if "TODO" in text or "FIXME" in text:
            violations.append(f"TODO/FIXME found in {p}")
    assert not violations, "TODO/FIXME comments present:\n" + "\n".join(violations)
