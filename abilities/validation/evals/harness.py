from typing import Any, Dict, List
import re
import httpx


async def generate(api_host: str, api_port: int, model: str, prompt: str, timeout: float = 30.0) -> str:
    url = f"http://{api_host}:{api_port}/api/generate"
    payload = {"model": model, "prompt": prompt, "stream": False, "max_tokens": 256}
    async with httpx.AsyncClient(timeout=timeout) as client:
        resp = await client.post(url, json=payload)
        resp.raise_for_status()
        try:
            body = resp.json()
        except ValueError:
            return resp.text.strip()

    # try several common response shapes
    if isinstance(body, dict):
        for k in ("response", "output", "text", "result"):
            if k in body and isinstance(body[k], str):
                return body[k].strip()
        choices = body.get("choices")
        if isinstance(choices, list) and choices:
            first = choices[0]
            if isinstance(first, dict):
                for k in ("message", "text", "content", "response"):
                    if k in first and isinstance(first[k], str):
                        return first[k].strip()
    return str(body)


def evaluate_output(output: str, checks: Dict[str, Any]) -> Dict[str, Any]:
    """Evaluate output against checks. Supported checks:
    - contains: list of substrings that must appear
    - not_contains: list of substrings that must NOT appear (case-insensitive)
    - regex_not: list of regex patterns that must not match
    """
    result: Dict[str, Any] = {"passed": True, "errors": []}

    for s in checks.get("contains", []):
        if s not in output:
            result["passed"] = False
            result["errors"].append(f"missing required substring: {s}")

    for s in checks.get("not_contains", []):
        if re.search(re.escape(s), output, re.IGNORECASE):
            result["passed"] = False
            result["errors"].append(f"forbidden substring present: {s}")

    for pattern in checks.get("regex_not", []):
        if re.search(pattern, output):
            result["passed"] = False
            result["errors"].append(f"forbidden regex matched: {pattern}")

    return result


async def run_cases(host: str, port: int, model: str, cases: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    results = []
    for case in cases:
        prompt = case["prompt"]
        output = await generate(host, port, model, prompt)
        eval_result = evaluate_output(output, case.get("checks", {}))
        results.append({"name": case.get("name"), "output": output, "result": eval_result})
    return results
