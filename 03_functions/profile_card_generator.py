def build_profile_card(**kwargs):
    lines = []
    
    for key, value in kwargs.items():
        formatted_key = key.capitalize()
        lines.append(f"{formatted_key}: {value}")
        
    return "\n".join(lines)


print(build_profile_card(city="Paphos", language="Python"))

print(build_profile_card(role="Developer", status="Active"))