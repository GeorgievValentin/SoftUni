fuel_type = input()
liters = float(input())
card = input()
price = 0

if fuel_type == "Diesel":
    price = 2.33
    if card == "Yes":
        price -= 0.12
elif fuel_type == "Gasoline":
    price = 2.22
    if card == "Yes":
        price -= 0.18
elif fuel_type == "Gas":
    price = 0.93
    if card == "Yes":
        price -= 0.08
cost = liters * price
if 20 <= liters <= 25:
    cost *= 0.92
elif liters > 25:
    cost *= 0.9
print(f"{cost:.2f} lv.")