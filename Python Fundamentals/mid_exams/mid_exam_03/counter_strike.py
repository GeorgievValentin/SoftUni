def print_result(final_energy: int, final_count: int, won: bool):
    if won:
        return f"Won battles: {final_count}. Energy left: {final_energy}"
    return f"Not enough energy! Game ends with {final_count} won battles and {final_energy} energy"


def increase_energy(energy: int, counter: int):
    if counter % 3 == 0:
        energy += counter
    return energy


def counter_strike(energy: int):
    counter = 0
    won_game = False
    while True:
        command = input()
        if command == "End of battle":
            won_game = True
            break

        distance = int(command)
        if energy >= distance:
            energy -= distance
            counter += 1
            energy = increase_energy(energy, counter)
        else:
            break
    result = print_result(energy, counter, won_game)
    return result


energy_ = int(input())

print(counter_strike(energy_))
