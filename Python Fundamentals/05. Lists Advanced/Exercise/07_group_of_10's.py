nums = [int(num) for num in input().split(", ")]
max_num = max(nums)
group = 10

if max_num % 10 == 0:
    max_boundary = max_num
else:
    max_boundary = (max_num // 10) * 10 + 10

while group <= max_boundary:
    nums_group = [num for num in nums if num in range(group-9, group+1)]
    print(f"Group of {group}'s: {nums_group}")
    group += 10


