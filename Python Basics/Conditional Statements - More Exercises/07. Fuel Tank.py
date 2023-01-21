fuel_type = input()
liters = float(input())

if fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type == "Gas":
    if liters < 25:
        print(f"Fill your tank with {fuel_type.lower()}!")
    else:
        print(f"You have enough {fuel_type.lower()}.")
else:
    print("Invalid fuel!")