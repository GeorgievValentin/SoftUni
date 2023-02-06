orders_count = int(input())
total_cost = 0
cost_for_order = 0

for order in range(orders_count):
    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if 0.01 <= capsule_price <= 100.00 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000:
        cost_for_order = capsule_price * days * capsules_per_day
        total_cost += cost_for_order
    if not cost_for_order <= 0:
        print(f"The price for the coffee is: ${cost_for_order:.2f}")
print(f"Total: ${total_cost:.2f}")
