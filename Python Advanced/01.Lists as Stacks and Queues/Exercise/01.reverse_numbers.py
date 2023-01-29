nums_list = input().split()
stack_nums = []

while nums_list:
    stack_nums.append(nums_list.pop())
print(" ".join(stack_nums))

#  print(" ".join(reversed(input().split())))
