nums = list(map(int, input().split(", ")))
index_list = [index for index in range(len(nums)) if nums[index] % 2 == 0]
print(index_list)
