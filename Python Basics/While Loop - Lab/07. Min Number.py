from sys import maxsize
operation = input()
smallest_num = maxsize
num = 0
while operation != "Stop":
    num = int(operation)
    if num < smallest_num:
        smallest_num = num
    operation = input()
print(f"{smallest_num}")
