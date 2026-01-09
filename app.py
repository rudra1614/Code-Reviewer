from admin import upload_main_code
from developer import push_code

def main():
    role = input("Login as (admin/developer): ").strip().lower()

    print("\nPaste your Python code. End with 'EOF'\n")

    lines = []
    while True:
        line = input()
        if line == "EOF":
            break
        lines.append(line)

    code = "\n".join(lines)

    if role == "admin":
        upload_main_code(code)
    elif role == "developer":
        push_code(code)
    else:
        print("❌ Invalid role")

if __name__ == "__main__":
    main()
