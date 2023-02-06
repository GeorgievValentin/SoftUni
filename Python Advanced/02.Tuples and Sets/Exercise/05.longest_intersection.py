import re
total_result = []
num = int(input())
data = []
for _ in range(num):
    ranges = re.split(",|-", input())
    ranges = [int(el) for el in ranges]

    first_start = ranges[0]
    first_end = ranges[1]
    second_start = ranges[2]
    second_end = ranges[3]
    range1 = set()
    range2 = set()
    for num1 in range(first_start, first_end + 1):
        range1.add(num1)
    for num2 in range(second_start, second_end + 1):
        range2.add(num2)
    result = range1.intersection(range2)
    if len(result) > len(total_result):
        total_result = list(result)
print(f"Longest intersection is {total_result} with length {len(total_result)}")
