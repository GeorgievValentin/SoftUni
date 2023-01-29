nums = (float(el) for el in input().split())
result = {}
for num in nums:
    if num not in result:
        result[num] = 0
    result[num] += 1
for key, value in result.items():
    print(f"{key} - {value} times")
    