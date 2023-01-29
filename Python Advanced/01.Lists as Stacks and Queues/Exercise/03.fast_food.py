from collections import deque

food_quantity = int(input())
orders = [int(el) for el in input().split()]  # orders = deque(map(int, input().split()))
orders_queue = deque(orders)
print(max(orders_queue))
while orders_queue:
    if food_quantity >= orders_queue[0]:
        food_quantity -= orders_queue.popleft()
    else:
        break
if not orders_queue:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(str(el) for el in orders_queue)}")