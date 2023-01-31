from collections import deque

bowls = [int(x) for x in input().split(", ")]
customers = deque(int(x) for x in input().split(", "))

while bowls and customers:
    current_bowl = bowls.pop()
    current_customer = customers.popleft()

    if current_bowl == current_customer:
        continue
    elif current_bowl > current_customer:
        bowls.append(current_bowl - current_customer)
    elif current_customer > current_bowl:
        customers.appendleft(current_customer - current_bowl)

if not customers:
    print("Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
