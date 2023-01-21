kilometers = int(input())
day_part = input()
price = 0
cost = 0

if kilometers >= 100:
    price = 0.06
elif kilometers >= 20:
    price = 0.09
else:
    cost += 0.7
    if day_part == "day":
        price = 0.79
    else:
        price = 0.9

cost += kilometers * price
print(f"{cost:.2f}")