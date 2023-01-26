num1 = int(input())
num2 = int(input())
number = int(input())
count = 0
combination = False
for i in range(num1, num2 + 1):
    for j in range(num1, num2 + 1):
        count += 1
        if i + j == number:
            combination = True
            break
    if combination:
        break
if combination:
    print(f"Combination N:{count} ({i} + {j} = {number})")
else:
    print(f"{count} combinations - neither equals {number}")