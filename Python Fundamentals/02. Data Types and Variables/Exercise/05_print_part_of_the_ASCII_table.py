first_number = int(input())
last_number = int(input())

for num in range(first_number, last_number + 1):
    print(f"{chr(num)}", end=" ")