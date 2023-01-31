size = 8
matrix = []

white_position = ()
black_position = ()

for row in range(size, 0, -1):
    line = input().split()
    matrix.append(line)
    if "w" in line:
        white_position = [row, line.index("w")]
    if "b" in line:
        black_position = [row, line.index("b")]

while True:
    if white_position[0] == black_position[0] - 1 and (
            white_position[1] == black_position[1] - 1 or white_position[1] == black_position[1] + 1):
        print(f"Game over! White win, capture on {chr(black_position[1] + 97)}{black_position[0]}.")
        break
    white_position[0] += 1
    if white_position[0] == 8:
        print(f"Game over! White pawn is promoted to a queen at {chr(white_position[1] + 97)}{white_position[0]}.")
        break
    if black_position[0] == white_position[0] + 1 and (
            black_position[1] == white_position[1] - 1 or black_position[1] == white_position[1] + 1):
        print(f"Game over! Black win, capture on {chr(white_position[1] + 97)}{white_position[0]}.")
        break
    black_position[0] -= 1
    if black_position[0] == 1:
        print(f"Game over! Black pawn is promoted to a queen at {chr(black_position[1] + 97)}{black_position[0]}.")
        break
