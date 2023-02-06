rows, cols = [int(x) for x in input().split()]

matrix = []
for i in range(rows):
    data = input().split()
    matrix.append(data)

while True:
    command = input()
    if command == "END":
        break
    action = command.split()

    if not action[0] == "swap" or not len(action) == 5:
        print("Invalid input!")
        continue
    indexes = [int(x) for x in action[1: len(action)]]
    row1, col1, row2, col2 = indexes[:]

    if row1 >= rows or row1 < 0 or row2 >= rows or row2 < 0 or col1 >= cols or col1 < 0 or col2 >= cols or col2 < 0:
        print("Invalid input!")
        continue
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    for el in matrix:
        print(" ".join(str(x) for x in el))


