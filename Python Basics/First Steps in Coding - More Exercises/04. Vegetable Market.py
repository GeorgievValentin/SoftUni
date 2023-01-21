vegetable_price = float(input())
fruit_price = float(input())
vegetable_kilos = float(input())
fruit_weight = float(input())
total = (vegetable_price * vegetable_kilos + fruit_price * fruit_weight) / 1.94
print(f"{total:.2f}")