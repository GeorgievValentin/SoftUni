def move_right(row, col):
    return row, col + 1


def move_up(row, col):
    return row - 1, col


def move_left(row, col):
    return row, col - 1


def move_down(row, col):
    return row + 1, col


size = int(input())
matrix = []
start_row = 0
start_col = 0
for row in range(size):
    elements = input().split()
    matrix.append(elements)
    for col in range(size):
        if elements[col] == "B":
            start_row = row
            start_col = col

directions = {
    "right": move_right,
    "up": move_up,
    "left": move_left,
    "down": move_down
}

best_score = float("-inf")
best_direction = ""
best_trace = []
for direction, step in directions.items():
    current_row, current_col = start_row, start_col
    current_score = 0
    current_trace = []

    while True:
        current_row, current_col = step(current_row, current_col)

        if not 0 <= current_row < size or not 0 <= current_col < size:
            break
        if matrix[current_row][current_col] == "X":
            break
        current_trace.append([current_row, current_col])
        current_score += int(matrix[current_row][current_col])

    if current_score > best_score:
        best_score = current_score
        best_direction = direction
        best_trace = current_trace

print(best_direction)
for el in best_trace:
    print(el)
print(best_score)