def next_position(direction, row, col):
    if direction == "up":
        return row - 1, col
    if direction == "down":
        return row + 1, col
    if direction == "left":
        return row, col - 1
    if direction == "right":
        return row, col + 1


presents = int(input())
size = int(input())
matrix = []

santa_row = 0
santa_col = 0
total_good_kids = 0
delivered_to_good_kids = 0

for row in range(size):
    line = input().split()
    matrix.append(line)

    if "S" in line:
        santa_row, santa_col = row, line.index("S")
    total_good_kids += line.count("V")

while True:
    command = input()
    if command == "Christmas morning":
        break

    matrix[santa_row][santa_col] = "-"
    santa_row, santa_col = next_position(command, santa_row, santa_col)
    if matrix[santa_row][santa_col] == "V":
        presents -= 1
        delivered_to_good_kids += 1
    elif matrix[santa_row][santa_col] == "C":
        if matrix[santa_row][santa_col - 1] == "V" and presents:
            delivered_to_good_kids += 1
            presents -= 1
            matrix[santa_row][santa_col - 1] = "-"
        elif matrix[santa_row][santa_col - 1] == "X" and presents:
            pass

        if matrix[santa_row][santa_col + 1] == "V" and presents:
            delivered_to_good_kids += 1
            presents -= 1
            matrix[santa_row][santa_col + 1] = "-"
        elif matrix[santa_row][santa_col + 1] == "X" and presents:
            presents -= 1
            matrix[santa_row][santa_col + 1] = "-"

        if matrix[santa_row - 1][santa_col] == "V" and presents:
            delivered_to_good_kids += 1
            presents -= 1
            matrix[santa_row - 1][santa_col] = "-"
        elif matrix[santa_row - 1][santa_col] == "X" and presents:
            presents -= 1
            matrix[santa_row - 1][santa_col] = "-"

        if matrix[santa_row + 1][santa_col] == "V" and presents:
            delivered_to_good_kids += 1
            presents -= 1
            matrix[santa_row + 1][santa_col] = "-"
        elif matrix[santa_row + 1][santa_col] == "X" and presents:
            presents -= 1
            matrix[santa_row + 1][santa_col] = "-"

    matrix[santa_row][santa_col] = "S"

    if presents == 0 or delivered_to_good_kids == total_good_kids:
        break

if presents == 0 and delivered_to_good_kids < total_good_kids:
    print("Santa ran out of presents!")

for row in matrix:
    print(*row, sep=" ")

if delivered_to_good_kids < total_good_kids:
    print(f"No presents for {total_good_kids - delivered_to_good_kids} nice kid/value.")
else:
    print(f"Good job, Santa! {total_good_kids} happy nice kid/value.")
