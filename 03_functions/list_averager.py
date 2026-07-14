def calculate_average(numbers):
    if not numbers:  
        return 0.0
    return sum(numbers) / len(numbers)

# Testing it
print(calculate_average([10, 20, 30]))  