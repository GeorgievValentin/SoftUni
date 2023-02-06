from collections import deque

chocolates = deque(int(x) for x in input().split(", "))
milks = deque(int(x) for x in input().split(", "))
milkshakes = 0
# print(chocolates)
# print(milks)

while milks and chocolates and milkshakes < 5:
    current_chocolate = chocolates.pop()
    current_milk = milks.popleft()
    if current_chocolate <= 0 and current_milk <= 0:
        continue
    if current_chocolate <= 0:
        milks.appendleft(current_milk)
        continue
    if current_milk <= 0:
        chocolates.append(current_chocolate)
        continue
    if current_chocolate == current_milk:
        milkshakes += 1
    else:
        chocolates.append(current_chocolate - 5)
        milks.append(current_milk)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print("Chocolate: empty")
if milks:
    print(f"Milk: {', '.join(str(x) for x in milks)}")
else:
    print("Milk: empty")

