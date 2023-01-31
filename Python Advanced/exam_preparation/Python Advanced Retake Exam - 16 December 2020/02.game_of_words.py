text = input()
size = int(input())
matrix = []

row = 0
col = 0

for r in range(size):
    data = input()
    line = []
    for el in data:
        line.append(el)
    matrix.append(line)

    if "P" in line:
        row = r
        col = line.index("P")
matrix[row][col] = "-"

num = int(input())

for _ in range(num):
    direction = input()

    if direction == "up":
        if row > 0:
            row -= 1
        else:
            text = text[:-1]
            continue

    if direction == "down":
        if row < size:
            row += 1
        else:
            text = text[:-1]
            continue

    if direction == "left":
        if col > 0:
            col -= 1
        else:
            text = text[:-1]
            continue

    if direction == "right":
        if col < size:
            col += 1
        else:
            text = text[:-1]
            continue

    if not matrix[row][col] == "-" and not matrix == "P":
        text += matrix[row][col]
        matrix[row][col] = "-"

matrix[row][col] = "P"

print(text)
for el in matrix:
    print("".join(el))


