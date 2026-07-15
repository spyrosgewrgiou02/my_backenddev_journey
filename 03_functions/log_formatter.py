def log_message(message: str, level = "INFO"):
    lvl = level.upper()
    return f"[{lvl}] {message}"
    
a = "System Started"
b = "Database Failed"
c = "error"

print(log_message(a))
print(log_message(b, c))