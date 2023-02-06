def calculate_result_by_operator(num1, num2, operation):
    if operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 // num2
    elif operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2


op = input()
n1 = int(input())
n2 = int(input())
result = calculate_result_by_operator(n1, n2, op)
print(result)