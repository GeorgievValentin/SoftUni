rows, cols = [int(x) for x in input().split(", ")]

matrix = []
result = 0
for _ in range(rows):
    data = [int(x) for x in input().split(", ")]
    matrix.append(data)
    result += sum(data)
print(result)
print(matrix)
