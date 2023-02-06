# def sum_numbers(num1, num2):
#     result = num1 + num2
#     return result
#
#
# def subtract(result, num3):
#     result_1 = result - num3
#     return result_1

def add_and_subtract(num1, num2, num3):
    return num1 + num2 - num3


n1 = int(input())
n2 = int(input())
n3 = int(input())
# sum_result = sum_numbers(n1, n2)
# total_result = subtract(sum_result, n3)
# print(total_result)
result = add_and_subtract(n1, n2, n3)
print(result)