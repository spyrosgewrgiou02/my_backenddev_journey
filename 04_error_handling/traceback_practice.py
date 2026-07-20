# Exercise 19: Resolving NameError
def greet_user(current_user: str) -> str:
    return f"Welcome back, {current_user}"


# Exercise 20: Resolving TypeError
def apply_coupon(total: float, discount_amount: float) -> float:
    return total - float(discount_amount)


user = "Spyros"
cart_total = 100.0
coupon = "15.5"

print(greet_user(user))
print(f"New Total: ${apply_coupon(cart_total, coupon)}")