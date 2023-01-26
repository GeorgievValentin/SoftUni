men = int(input())
women = int(input())
tables = int(input())


while True:
    for m in range(1, men + 1):
        for w in range(1, women + 1):
            if tables == 0:
                break
            tables -= 1
            print(f"({m} <-> {w})", end=" ")
    if m == men or w == women:
        break