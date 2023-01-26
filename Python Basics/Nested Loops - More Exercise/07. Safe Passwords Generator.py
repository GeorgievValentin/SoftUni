a = int(input())
b = int(input())
max_passwords = int(input())
counter = 0
A = 35
B = 64

for x in range(1, a + 1):
    for y in range(1, b + 1):
        counter += 1
        if counter > max_passwords:
            break
        if A > 55:
            A = 35
        if B > 96:
            B = 64
        print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}",end="|")
        A += 1
        B += 1