from config import MODEL
from security import run_security_scan
import difflib

MAIN_CODE_PATH = "storage/main_code.py"

def load_main_code():
    try:
        with open(MAIN_CODE_PATH) as f:
            return f.read()
    except FileNotFoundError:
        return None

def generate_diff(old, new):
    return "\n".join(difflib.unified_diff(
        old.splitlines(),
        new.splitlines(),
        lineterm=""
    ))

def ai_review(old_code, new_code, diff, security_issues):
    prompt = f"""
You are a senior DevSecOps engineer.

Analyze the following code change.

OLD CODE:
{old_code}

NEW CODE:
{new_code}

DIFF:
{diff}

SECURITY ISSUES:
{security_issues}

Tasks:
1. Identify NEW bugs introduced by the change
2. Identify runtime crash risks
3. Identify backward compatibility issues
4. Identify performance regressions
5. Suggest fixes
6. Decide: SAFE_TO_MERGE (YES/NO)

Respond in structured bullet points.
"""
    return MODEL.generate_content(prompt).text

def gatekeep(new_code: str):
    old_code = load_main_code()
    if not old_code:
        return False, "❌ No main program uploaded by admin."

    security_issues = run_security_scan(new_code)
    diff = generate_diff(old_code, new_code)

    ai_report = ai_review(old_code, new_code, diff, security_issues)

    decision = "NO" not in ai_report.upper()

    return decision, ai_report
