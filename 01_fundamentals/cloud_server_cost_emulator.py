print("=" * 30)
print("The Cloud Server Cost Emulator: ")
print("=" * 30)
print("\n")

name = str(input("name of the cloud service: "))
cost = float(input(f"Cost per hour to run the {name} service: "))
hours = int(input(f"how many hours does the {name} service run per day?: "))

final_cst = cost * hours

print(f"\n the {name} costs {final_cst} euros per day to run.")