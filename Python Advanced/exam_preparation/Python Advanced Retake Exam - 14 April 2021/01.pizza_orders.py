from collections import deque

orders = deque(int(x) for x in input().split(", "))
capacities = [int(x) for x in input().split(", ")]

pizzas_made = 0

while capacities and orders:
    order = orders.popleft()

    if order <= 0 or order > 10:
        continue

    capacity = capacities.pop()

    if order <= capacity:
        pizzas_made += order

    else:
        orders.appendleft(order - capacity)
        pizzas_made += capacity

if not orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizzas_made}")
    if capacities:
        print(f"Employees: {', '.join(str(x) for x in capacities)}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in orders)}")
