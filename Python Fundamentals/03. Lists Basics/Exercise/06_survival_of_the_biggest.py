nums_string = input().split()
nums_to_remove = int(input())
nums = []
for num in nums_string:
    nums.append(int(num))

for _ in range(nums_to_remove):
    nums.remove(min(nums))
print(*nums, sep=", ")
