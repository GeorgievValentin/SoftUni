n = int(input())
matrix = []

for _ in range(n):
    matrix.extend(int(x) for x in input().split(", "))
print(matrix)
