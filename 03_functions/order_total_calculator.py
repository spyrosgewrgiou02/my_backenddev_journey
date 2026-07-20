def calculate_order_total(customer_name, **items):
    total_spend = 0.0
    
    for price in items.values():
        total_spend += price
        
    return f"{customer_name}'s Total: {total_spend}"

print(calculate_order_total("Spyros", coffee=3.50, sandwich=5.00))

print(calculate_order_total("Spyros"))
