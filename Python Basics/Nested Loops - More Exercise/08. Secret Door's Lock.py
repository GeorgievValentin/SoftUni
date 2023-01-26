max_a = int(input())
max_b = int(input())
max_c = int(input())

for a in range(2, max_a + 1, 2):
    for b in range(2, max_b + 1):
        for c in range(2, max_c + 1, 2):
            if b == 2 or b == 3 or b == 5 or b == 7:
                print(f"{a} {b} {c}")
