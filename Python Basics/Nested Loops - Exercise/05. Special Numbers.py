number = int(input())
for num in range(1111, 9999 + 1):
    special = True
    num_as_string = str(num)
    for digit in num_as_string:
        if int(digit) == 0 or number % int(digit) != 0:
            special = False
    if special:
        print(num, end=" ")
