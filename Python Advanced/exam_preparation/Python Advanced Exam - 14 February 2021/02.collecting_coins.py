size = int(input())
matrix = []
row = 0
col = 0
path = []
coins = 0
directions = ["up", "down", "left", "right"]
hit_wall = False

for r in range(size):
    line = [int(x) if x.isdigit() else x for x in input().split()]
    matrix.append(line)
    if "P" in line:
        row = r
        col = line.index("P")
        path.append([row, col])
        matrix[row][col] = 0

while True:
    direction = input()
    if direction not in directions:
        continue

    if direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    elif direction == "left":
        col -= 1
    elif direction == "right":
        col += 1

    if row < 0:
        row = size - 1
    if row == size:
        row = 0
    if col < 0:
        col = size - 1
    if col == size:
        col = 0

    path.append([row, col])

    if matrix[row][col] == "X":
        coins //= 2
        hit_wall = True
        break

    else:
        coins += matrix[row][col]
        matrix[row][col] = 0

    if coins >= 100:
        break

if hit_wall:
    print(f"Game over! You've collected {coins} coins.")
else:
    print(f"You won! You've collected {coins} coins.")
print("Your path:")
print(*path, sep="\n")
