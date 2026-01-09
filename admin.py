import os

MAIN_CODE_PATH = "storage/main_code.py"

def upload_main_code(code: str):
    os.makedirs("storage", exist_ok=True)
    with open(MAIN_CODE_PATH, "w") as f:
        f.write(code)
    print("✅ Main program uploaded successfully.")
