from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())
result = 0

while bees and nectar:
    current_bee = bees[0]
    current_nectar = nectar.pop()
    if current_nectar < current_bee:
        continue
    bees.popleft()
    current_symbol = symbols.popleft()
    if current_symbol == "+":
        result += abs(current_bee + current_nectar)
    elif current_symbol == "-":
        result += abs(current_bee - current_nectar)
    elif current_symbol == "*":
        result += abs(current_bee * current_nectar)
    elif current_symbol == "/" and not current_nectar == 0:
        result += abs(current_bee / current_nectar)

print(f"Total honey made: {result}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
