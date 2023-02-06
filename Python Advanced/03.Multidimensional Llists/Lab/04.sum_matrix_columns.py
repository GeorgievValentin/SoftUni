rows, cols = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(rows):
    nums = [int(x) for x in input().split()]
    matrix.append(nums)
for i in range(cols):
    result = 0
    for j in range(rows):
        result += matrix[j][i]
    print(result)
