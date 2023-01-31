rows, cols = [int(x) for x in input().split(", ")]

matrix = []
merry_christmas = False

decorations = 0
gifts = 0
cookies = 0

d = 0
g = 0
c = 0

for row in range(rows):
    line = input().split()
    matrix.append(line)
    if "Y" in line:
        pos_row = row
        pos_col = line.index("Y")

    d += line.count("D")
    g += line.count("G")
    c += line.count("C")

matrix[pos_row][pos_col] = "x"
command = input()

while not command == "End":
    data = command.split("-")
    direction = data[0]
    steps = int(data[1])

    for _ in range(steps):

        if direction == "up":
            pos_row -= 1
        elif direction == "down":
            pos_row += 1
        elif direction == "left":
            pos_col -= 1
        elif direction == "right":
            pos_col += 1

        if pos_row >= rows:
            pos_row -= rows
        if pos_row < 0:
            pos_row += rows
        if pos_col >= cols:
            pos_col -= cols
        if pos_col < 0:
            pos_col += cols

        if matrix[pos_row][pos_col] == "D":
            decorations += 1
            d -= 1
        if matrix[pos_row][pos_col] == "G":
            gifts += 1
            g -= 1
        if matrix[pos_row][pos_col] == "C":
            cookies += 1
            c -= 1

        matrix[pos_row][pos_col] = "Y"

        if d == 0 and g == 0 and c == 0:
            merry_christmas = True
            break
        matrix[pos_row][pos_col] = "x"

    if merry_christmas:
        break

    command = input()
    if command == "End":
        matrix[pos_row][pos_col] = "Y"

if merry_christmas:
    print("Merry Christmas!")

print("You've collected:")
print(f"- {decorations} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")

for el in matrix:
    print(" ".join(el))


