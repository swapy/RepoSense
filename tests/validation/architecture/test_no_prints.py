import ast
from pathlib import Path


def _py_files():
    repo_root = Path(__file__).resolve()
    while repo_root != repo_root.parent and not (repo_root / "pyproject.toml").exists():
        repo_root = repo_root.parent
    for p in repo_root.rglob("*.py"):
        # skip tests directory
        if "tests/validation" in str(p):
            continue
        yield p


def test_no_print_statements():
    violations = []
    for p in _py_files():
        try:
            tree = ast.parse(p.read_text(encoding="utf-8"))
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                func = node.func
                if isinstance(func, ast.Name) and func.id == "print":
                    violations.append(f"print() found in {p}")
    assert not violations, "print() usage found; prefer logging: \n" + "\n".join(violations)
