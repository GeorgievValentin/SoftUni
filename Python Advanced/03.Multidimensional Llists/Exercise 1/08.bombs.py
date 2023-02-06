n = int(input())
matrix = []

for _ in range(n):
    nums = [int(x) for x in input().split()]
    matrix.append(nums)

coordinates = input().split()
for bomb in coordinates:
    row, col = [int(x) for x in bomb.split(",")]
    bomb_power = matrix[row][col]
    
