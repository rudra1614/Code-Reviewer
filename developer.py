from gatekeeper import gatekeep

def push_code(code: str):
    allowed, report = gatekeep(code)

    print("\n📋 AI FINAL REPORT:\n")
    print(report)

    if allowed:
        with open("storage/main_code.py", "w") as f:
            f.write(code)
        print("\n✅ CODE MERGED INTO MAIN PROGRAM")
    else:
        print("\n❌ CODE REJECTED — FIX REQUIRED")
