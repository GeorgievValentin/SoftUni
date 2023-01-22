num_1 = int(input())
num_2 = int(input())
operation = input()
result = 0
if operation == "+":
    result = num_1 + num_2
elif operation == "-":
    result = num_1 - num_2
elif operation == "*":
    result = num_1 * num_2
elif operation == "/":
    if num_2 == 0:
        print(f"Cannot divide {num_1} by zero")
    else:
        result = num_1 / num_2
        print(f"{num_1} / {num_2} = {result:.2f}")
elif operation == "%":
    if num_2 == 0:
        print(f"Cannot divide {num_1} by zero")
    else:
        result = num_1 % num_2
        print(f"{num_1} % {num_2} = {result}")
if operation == "+" or operation == "-" or operation == "*":
    if result % 2 == 0:
        print(f"{num_1} {operation} {num_2} = {result} - even")
    else:
        print(f"{num_1} {operation} {num_2} = {result} - odd")