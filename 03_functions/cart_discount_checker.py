def is_eligible_for_discount(subtotal: float, minimum_spend: float = 50.0) -> bool:
    return subtotal >= minimum_spend


def apply_discount(subtotal: float, discount_percent: float = 10.0) -> float:
    return subtotal * (1 - (discount_percent / 100))


cart_total = 75.0

if is_eligible_for_discount(cart_total):
    final_price = apply_discount(cart_total)
    print(f"Discount applied! Final total: {final_price}")
else:
    print(f"Total: {cart_total}")