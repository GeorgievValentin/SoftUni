num = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
count = 0
cost = 0

for i in range(1, num + 1):
    if i % 2 == 0:
        cost += helmet_price
    if i % 3 == 0:
        cost += sword_price
    if i % 2 == 0 and i % 3 == 0:
        cost += shield_price
        count += 1
        if count % 2 == 0:
            cost += armor_price
print(f"Gladiator expenses: {cost:.2f} aureus")