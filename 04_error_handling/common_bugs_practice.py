# Exercise 23: Fixing Scope Bugs (Passing Arguments)
def process_withdrawal(current_balance: float, amount: float) -> str:
    new_balance = current_balance - amount
    return f"New balance: ${new_balance:.2f}"


# Exercise 24: Fixing Type Bugs (Using F-Strings)
def generate_invoice(item: str, quantity: int, price_per_unit: float) -> str:
    total = quantity * price_per_unit
    return f"Item: {item} | Quantity: {quantity} | Total: ${total:.2f}"


# --- Verification Runs ---
if __name__ == "__main__":
    print("--- Scope Fix Test ---")
    initial_balance = 100.0
    print(process_withdrawal(initial_balance, 20.0))

    print("\n--- Type Fix Test ---")
    print(generate_invoice("Mechanical Keyboard", 2, 85.0))