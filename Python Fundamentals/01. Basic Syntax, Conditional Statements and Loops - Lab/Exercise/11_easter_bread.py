budget = float(input())
flour_price_1kg = float(input())
eggs_price = flour_price_1kg * 0.75
milk_price_1l = flour_price_1kg * 1.25

bread_price = flour_price_1kg + eggs_price + milk_price_1l * 0.25
bread_count = 0
colored_eggs = 0

while budget >= bread_price:
    budget -= bread_price
    bread_count += 1
    colored_eggs += 3
    if bread_count % 3 == 0:
        colored_eggs -= (bread_count - 2)
print(f"You made {bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

