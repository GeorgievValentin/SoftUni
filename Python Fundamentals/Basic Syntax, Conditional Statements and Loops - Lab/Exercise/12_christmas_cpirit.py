quantity = int(input())
days = int(input())

ornament_set = 2
skirt = 5
garlands = 3
lights = 15

christmas_spirit = 0
cost = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        cost += ornament_set * quantity
        christmas_spirit += 5
    if day % 3 == 0:
        cost += (skirt * quantity + garlands * quantity)
        christmas_spirit += 13
    if day % 5 == 0:
        cost += lights * quantity
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30

    if day % 10 == 0:
        christmas_spirit -= 20
        cost += lights + garlands + skirt

    if day == days and day % 10 == 0:
        christmas_spirit -= 30

print(f"Total cost: {cost}")
print(f"Total spirit: {christmas_spirit}")