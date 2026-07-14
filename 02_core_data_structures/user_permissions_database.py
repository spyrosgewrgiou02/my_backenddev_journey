usr = {"username": "blakewinston99", "email": "blakeyw99@gmail.com", "is_active": True, "role": "Backend Developer"}

if usr["is_active"] and usr["role"] == "admin":
    print("Full System Access")
else:
    print("Access Denied")