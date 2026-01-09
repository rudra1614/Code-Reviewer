import subprocess
import tempfile
import json
import os

def run_security_scan(code: str):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as f:
        f.write(code.encode())
        path = f.name

    result = subprocess.run(
        ["bandit", "-f", "json", path],
        capture_output=True,
        text=True
    )

    os.unlink(path)

    if result.stdout:
        return json.loads(result.stdout).get("results", [])
    return []
