num1 = int(input())
num2 = int(input())
for curent_num in range(num1, num2 + 1):
    odd_digits = 0
    even_digits = 0
    num_as_string = str(curent_num)
    for index, digits in enumerate(num_as_string):
        if index % 2 == 0:
            odd_digits += int(digits)
        else:
            even_digits += int(digits)
    if odd_digits == even_digits:
        print(curent_num, end=" ")

num1 = int(input())
num2 = int(input())

for i in range(num1, num2 + 1):
    odd_digits = 0
    even_digits = 0
