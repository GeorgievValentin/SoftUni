size = 6
matrix = []
row, col = 0, 0
deposits = {"water": 0, "metal": 0, "concrete": 0}
for i in range(size):
    line = input().split()
    matrix.append(line)
    if "E" in line:
        row = i
        col = line.index("E")

directions = input().split(", ")

for direction in directions:
    if direction == "up":
        row -= 1
        if row < 0:
            row = 5
        if row > 5:
            row = 0
    elif direction == "down":
        row += 1
        if row < 0:
            row = 5
        if row > 5:
            row = 0
    elif direction == "left":
        col -= 1
        if col < 0:
            col = 5
        if col > 5:
            col = 0
    elif direction == "right":
        col += 1
        if col < 0:
            col = 5
        if col > 5:
            col = 0

    if matrix[row][col] == "R":
        print(f"Rover got broken at ({row}, {col})")
        break
    elif matrix[row][col] == "W":
        deposits["water"] += 1
        print(f"Water deposit found at ({row}, {col})")
    elif matrix[row][col] == "M":
        deposits["metal"] += 1
        print(f"Metal deposit found at ({row}, {col})")
    elif matrix[row][col] == "C":
        deposits["concrete"] += 1
        print(f"Concrete deposit found at ({row}, {col})")

if deposits["water"] > 0 and deposits["metal"] > 0 and deposits["concrete"] > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
