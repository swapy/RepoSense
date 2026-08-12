from pathlib import Path
import re


def test_no_bare_except_blocks():
    repo_root = Path(__file__).resolve()
    while repo_root != repo_root.parent and not (repo_root / "pyproject.toml").exists():
        repo_root = repo_root.parent
    violations = []
    pattern = re.compile(r"^\s*except\s*:\s*(#.*)?$", re.MULTILINE)
    for p in repo_root.rglob("*.py"):
        if "tests/validation" in str(p):
            continue
        text = p.read_text(encoding="utf-8")
        if pattern.search(text):
            violations.append(f"bare except found in {p}")
    assert not violations, "Bare except blocks detected:\n" + "\n".join(violations)
