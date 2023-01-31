matrix = []
size = 6

player_1, player_2 = input().split(", ")

player_1_hit_wall = False
player_2_hit_wall = False

for _ in range(size):
    matrix.append(input().split())

while True:
    coordinates = input()

    if not player_1_hit_wall:
        row, col = int(coordinates[1]), int(coordinates[4])
        position = matrix[row][col]
        if position == "E":
            print(f"{player_1} found the Exit and wins the game!")
            break

        elif position == "T":
            print(f"{player_1} is out of the game! The winner is {player_2}.")
            break

        elif position == "W":
            print(f"{player_1} hits a wall and needs to rest.")
            player_1_hit_wall = True
    else:
        player_1_hit_wall = False

    coordinates = input()
    if not player_2_hit_wall:
        row, col = int(coordinates[1]), int(coordinates[4])
        position = matrix[row][col]
        if position == "E":
            print(f"{player_2} found the Exit and wins the game!")
            break

        elif position == "T":
            print(f"{player_2} is out of the game! The winner is {player_1}.")
            break

        elif position == "W":
            print(f"{player_2} hits a wall and needs to rest.")
            player_2_hit_wall = True
    else:
        player_2_hit_wall = False

