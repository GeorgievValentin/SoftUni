budget = float(input())
statists = int(input())
dress_price = float(input())

if statists > 150:
    dress_price *= 0.9
decor_price = budget * 0.1
total_dress_price = statists * dress_price
costs = total_dress_price + decor_price
difference = abs(budget - costs)
if budget >= costs:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")