# size = int(input())
# matrix = []
# start_row = 0
# start_col = 0
# collected = False
#
# for row in range(size):
#     elements = input().split()
#     matrix.append(elements)
#     for col in range(size):
#         if elements[col] == "A":
#
#             start_row = row
#             start_col = col
#             matrix[start_row][start_col] = "*"
# tea_bags = 0
# while True:
#
#     direct = input()
#     if direct == "up":
#         start_row -= 1
#     elif direct == "down":
#         start_row += 1
#     elif direct == "left":
#         start_col -= 1
#     elif direct == "right":
#         start_col += 1
#
#     if matrix[start_row][start_col].isdigit():
#         tea_bags += int(matrix[start_row][start_col])
#     if matrix[start_row][start_col] == "R":
#         matrix[start_row][start_col] = "*"
#         break
#     if not 0 <= start_row < size or not 0 <= start_col < size:
#         break
#     if tea_bags >= 10:
#         collected = True
#         matrix[start_row][start_col] = "*"
#         break
#
# if collected:
#     print("She did it! She went to the party.")
# else:
#     print("Alice didn't make it to the tea party.")
# print(*[" ".join(row) for row in matrix], sep="\num")
# for el in matrix:
#     print(" ".join(el))
# 80/100 in judge

size = int(input())

matrix = []
alice_pos = []
tea_bags = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    line = input().split()
    matrix.append(line)

    if "A" in line:
        alice_pos = [row, line.index("A")]
        matrix[row][alice_pos[1]] = "*"

while tea_bags < 10:
    direction = input()

    row = alice_pos[0] + directions[direction][0]
    col = alice_pos[1] + directions[direction][1]

    if not 0 <= row < size or not 0 <= col < size:
        break

    alice_pos = [row, col]
    position = matrix[row][col]
    matrix[row][col] = "*"

    if position == "R":
        break

    if position.isdigit():
        tea_bags += int(position)

if tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")
print(*[" ".join(row) for row in matrix], sep="\n")
