print("=" * 30)
print("The Security Gateway")
print("=" * 30)
print()

token = input("Please provide an API token: ").strip()

if not token:
    print("400 Bad Request: Token Missing")
elif token == "admin_root_99":
    print("200 OK: Admin Access Granted")
elif token == "user_basic_11":
    print("200 OK: Standard Access Granted")
else:
    print("401 Unauthorized: Invalid token.")