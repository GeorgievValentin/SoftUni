factor = int(input())
count = int(input())
list_numbers = []
for nums in range(factor, factor * count + 1, factor):
    list_numbers.append(nums)
print(list_numbers)
