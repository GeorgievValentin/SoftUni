flower_type = input()
flowers_count = int(input())
budget = int(input())
price = 0
if flower_type == "Roses":
    price = 5
    if flowers_count > 80:
        price *= 0.9
elif flower_type == "Dahlias":
    price = 3.8
    if flowers_count > 90:
        price *= 0.85
elif flower_type == "Tulips":
    price = 2.8
    if flowers_count > 80:
        price *= 0.85
elif flower_type == "Narcissus":
    price = 3
    if flowers_count < 120:
        price *= 1.15
elif flower_type == "Gladiolus":
    price = 2.5
    if flowers_count < 80:
        price *= 1.2
cost = flowers_count * price
diff = abs(cost - budget)
if budget >= cost:
    print(f"Hey, you have a great garden with {flowers_count} {flower_type} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")