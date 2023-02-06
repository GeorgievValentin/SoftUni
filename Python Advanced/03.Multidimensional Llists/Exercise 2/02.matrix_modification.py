n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

while True:
    command = input()
    if command == "END":
        break
    data = command.split()
    action = data[0]
    row, col, value = [int(x) for x in data[1:]]

    if not 0 <= row < n or not 0 <= col < len(matrix[0]):
        print("Invalid coordinates")
        continue
    if action == "Add":
        matrix[row][col] += value
    elif action == "Subtract":
        matrix[row][col] -= value
for el in matrix:
    print(" ".join(str(x) for x in el))
