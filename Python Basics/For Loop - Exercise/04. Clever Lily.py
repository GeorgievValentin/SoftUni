age = int(input())
machine_price = float(input())
toy_price = int(input())
money = 0
toys = 0
total_money = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        money += 10
        total_money += money - 1
    else:
        toys += 1
total_money += toys * toy_price
diff = abs(machine_price - total_money)
if machine_price > total_money:
    print(f"No! {diff:.2f}")
else:
    print(f"Yes! {diff:.2f}")
