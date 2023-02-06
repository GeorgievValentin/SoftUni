from math import factorial


def factorial_division(num1, num2):
    fact1 = factorial(num1)
    fact2 = factorial(num2)
    return fact1 / fact2


n1 = int(input())
n2 = int(input())
result = factorial_division(n1, n2)
print(f"{result:.2f}")

