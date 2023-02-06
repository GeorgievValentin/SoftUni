items = input().split("|")
current_budget = float(input())
new_prices = []
profit = 0
going_to_france = False
budget = current_budget

for item in items:
    item = item.split("->")
    typ = item[0]
    price = float(item[1])
    if typ == "Clothes" and price > 50:
        continue
    elif typ == "Shoes" and price > 35:
        continue
    elif typ == "Accessories" and price > 20.5:
        continue
    if price > budget:
        continue
    budget -= price
    price *= 1.4
    new_prices.append(str(price))
total_budget = 0
for prices in new_prices:
    total_budget += float(prices)

total_budget += budget
profit = total_budget - current_budget
if total_budget >= 150:
    going_to_france = True

for result in new_prices:
    print(f"{float(result):.2f}", end=" ")
print()

print(f"Profit: {profit:.2f}")
if going_to_france:
    print("Hello, France!")
else:
    print("Not enough money.")
