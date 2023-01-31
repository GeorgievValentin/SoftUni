from collections import deque

males = [int(x) for x in input().split()]
females = deque(int(x) for x in input().split())
matches = 0

while males and females:
    male = males.pop()
    if male <= 0:
        continue
    if male % 25 == 0:
        males.pop()
        continue

    female = females.popleft()
    if female <= 0:
        males.append(male)
        continue
    if female % 25 == 0:
        females.popleft()
        males.append(male)
        continue

    if male == female:
        matches += 1
    else:
        males.append(male - 2)
males.reverse()
print(f"Matches: {matches}")
print(f"Males left: {(', '.join(str(x) for x in males) if males else 'none')}")
print(f"Females left: {(', '.join(str(x) for x in females) if females else 'none')}")
