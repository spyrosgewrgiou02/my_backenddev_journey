# Exercise 26: List Comprehension
def convert_prices(prices, rate=0.92):
    return [round(price * rate, 2) for price in prices]


# Exercise 27: Dict Comprehension
def filter_premium_users(users_dict):
    return {user: tier for user, tier in users_dict.items() if tier == "premium"}


# --- Verification Runs ---
usd_prices = [10.0, 25.5, 99.99]
print("EUR Prices:", convert_prices(usd_prices))

users = {"spyros": "free", "alex": "premium", "maria": "premium"}
print("Premium Users:", filter_premium_users(users))