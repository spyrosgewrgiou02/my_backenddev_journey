def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * (9 / 5)) + 32


def format_temperature(temp: float, unit: str = "C") -> str:
    return f"{temp:.1f}°{unit.upper()}"


temp_c = 25.0
temp_f = celsius_to_fahrenheit(temp_c)

print(format_temperature(temp_c, "C"))
print(format_temperature(temp_f, "F"))