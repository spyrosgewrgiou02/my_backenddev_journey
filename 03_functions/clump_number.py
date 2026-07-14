def clamp_number(num, min_val, max_val):
    if num <= min_val:
        return min_val
    elif num >= max_val:
        return max_val
    return num

# Testing it
print(clamp_number(15, 1, 10)) 