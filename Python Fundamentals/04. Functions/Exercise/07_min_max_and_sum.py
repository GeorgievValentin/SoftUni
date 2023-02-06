nums = input().split()
int_nums = []
for num in nums:
    int_nums.append(int(num))
min_num = min(int_nums)
max_num = max(int_nums)
sum_nums = sum(int_nums)
print(f"The minimum number is {min_num}")
print(f"The maximum number is {max_num}")
print(f"The sum number is: {sum_nums}")
