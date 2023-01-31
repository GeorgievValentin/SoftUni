size = 6
matrix = []

for _ in range(size):
    line = input().split()
    matrix.append(line)

start_position = input()
row = int(start_position[1])
col = int(start_position[4])

command = input()

while not command == "Stop":
    split_command = command.split(", ")

    action = split_command[0]
    direction = split_command[1]
    if len(split_command) == 3:
        value = split_command[2]

    if direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    elif direction == "left":
        col -= 1
    elif direction == "right":
        col += 1

    if action == "Create":
        if matrix[row][col] == ".":
            matrix[row][col] = value

    if action == "Update":
        if not matrix[row][col] == ".":
            matrix[row][col] = value

    if action == "Delete":
        if not matrix[row][col] == ".":
            matrix[row][col] = "."

    if action == "Read":
        if not matrix[row][col] == ".":
            print(matrix[row][col])

    command = input()
for el in matrix:
    print(*el, sep=" ")
