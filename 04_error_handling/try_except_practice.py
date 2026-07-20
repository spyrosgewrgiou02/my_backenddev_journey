# Exercise 21: The Safe Calculator
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Inputs must be numbers"


# Exercise 22: The Dictionary Lookup
def get_user_age(user_data, key):
    try:
        return user_data[key]
    except KeyError:
        return "User detail not found"


# --- Verification Runs ---
if __name__ == "__main__":
    print("--- Safe Divide Tests ---")
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
    print(safe_divide(10, "2"))

    print("\n--- Dictionary Lookup Tests ---")
    user_info = {"name": "Spyros", "age": 25}
    print(get_user_age(user_info, "age"))
    print(get_user_age(user_info, "email"))