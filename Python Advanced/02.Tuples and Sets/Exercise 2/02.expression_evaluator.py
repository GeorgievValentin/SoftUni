from collections import deque

expression = input().split()

nums = deque()

for el in expression:
    if el in "+-*/":
        while len(nums) > 1:
            first_num = nums.popleft()
            second_num = nums.popleft()
            result = 0
            if el == "+":
                result = first_num + second_num
            elif el == "-":
                result = first_num - second_num
            elif el == "*":
                result = first_num * second_num
            else:
                result = first_num // second_num
            nums.appendleft(result)
    else:
        nums.append(int(el))
print(nums[0])
