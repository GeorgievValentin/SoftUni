def move(direction, steps):
    r = position[0] + (directions[direction][0] * steps)
    c = position[1] + (directions[direction][1] * steps)

    if not (0 <= r < size and 0 <= c < size):
        return position
    if matrix[r][c] == "x":
        return position
    return [r, c]


def shoot(direction):
    r = position[0] + directions[direction][0]
    c = position[1] + directions[direction][1]

    while 0 <= r < size and 0 <= c < size:
        if matrix[r][c] == "x":
            matrix[r][c] = "."
            return [r, c]
        r += directions[direction][0]
        c += directions[direction][1]


size = 5
matrix = []

position = []

targets = 0
hit_targets = 0
hit_targets_position = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    line = input().split()
    matrix.append(line)

    if "A" in line:
        position = [row, line.index("A")]
        matrix[row][position[1]] = "."
    targets += line.count("x")

for _ in range(int(input())):
    command = input().split()
    direction = command[1]
    if command[0] == "move":
        steps = int(command[2])
        position = move(direction, steps)
    else:
        target_down_pos = shoot(direction)

        if target_down_pos:
            hit_targets_position.append(target_down_pos)
            hit_targets += 1

        if hit_targets == targets:
            print(f"Training completed! All {targets} targets hit.")
            break

if hit_targets < targets:
    print(f"Training not completed! {targets - hit_targets} targets left.")
[print(targ_pos) for targ_pos in hit_targets_position]
