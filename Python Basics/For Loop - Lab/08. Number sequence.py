import sys
smallest = sys.maxsize
biggets = -sys.maxsize
nums = int(input())
for i in range(nums):
    number = int(input())
    if number < smallest:
        smallest = number
    if number > biggets:
        biggets = number
print(f"Max number: {biggets}")
print(f"Min number: {smallest}")