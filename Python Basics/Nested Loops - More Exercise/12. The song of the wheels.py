num = int(input())
counter = 0
passw = False
password = ""
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a * b + c * d == num and a < b and c > d:
                    counter += 1
                    print(f"{a}{b}{c}{d}", end=" ")
                    if counter == 4:
                        passw = True
                        password = f"{a}{b}{c}{d}"
print()
if passw:
    print(f"Password: {password}")
else:
    print("No!")