nums = [int(num) for num in input().split()]
result = 0
while nums:
    index = int(input())
    if index < 0:
        removed_num = nums.pop(0)
        nums.insert(0, nums[-1])
    elif index > len(nums) - 1:
        removed_num = nums.pop(-1)
        nums.insert(len(nums), nums[0])
    else:
        removed_num = nums.pop(index)
    for index, digit in enumerate(nums):
        if digit <= removed_num:
            nums[index] += removed_num
        else:
            nums[index] -= removed_num
    result += removed_num

print(result)