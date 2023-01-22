nums = int(input())
lefts = 0
rights = 0

for i in range(nums):
    lefts += int(input())
for i in range(nums):
    rights += int(input())
diff = abs(lefts - rights)
if lefts == rights:
    print(f"Yes, sum = {lefts}")
else:
    print(f"No, diff = {diff}")