nums = int(input())
sum = 0
diff = 0
for i in range(nums):
    num_1 = int(input())
    num_2 = int(input())
    curent_sum = num_1 + num_2
    if i == 0:
        sum = curent_sum
    else:
        if curent_sum != sum:
            curent_diff = abs(curent_sum - sum)
            sum = curent_sum
            if curent_diff > diff:
                diff = curent_diff
if diff == 0:
    print(f"Yes, value={sum}")
else:
    print(f"No, maxdiff={diff}")