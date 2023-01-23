from sys import  maxsize
operation = input()
bigest_num = -maxsize
num = 0
while operation != "Stop":
    num = int(operation)
    if num > bigest_num:
        bigest_num = num
    operation = input()
print(f"{bigest_num}")