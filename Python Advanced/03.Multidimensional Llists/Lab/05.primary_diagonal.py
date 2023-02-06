n = int(input())
matrix = []
result = 0

for _ in range(n):
    nums = [int(x) for x in input().split()]
    matrix.append(nums)

diagonal = 0
for index in range(n):
    diagonal += matrix[index][index]
print(diagonal)
