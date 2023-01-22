from sys import maxsize

nums = int(input())
sum = 0
biggest_num = -maxsize
for i in range(nums):
    number = int(input())
    if number > biggest_num:
        biggest_num = number
    sum += number
diff = abs(biggest_num - sum)
if biggest_num == sum - biggest_num:
    print("Yes")
    print(f"Sum = {biggest_num}")
else:
    sum -= biggest_num
    diff = abs(sum - biggest_num)
    print("No")
    print(f"Diff = {diff}")