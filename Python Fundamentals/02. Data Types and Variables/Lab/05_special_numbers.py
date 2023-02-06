number = int(input())

for num in range(1, number + 1):
    sum_digits = 0
    num_as_string = str(num)
    for numbers in num_as_string:
        sum_digits += int(numbers)
    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")