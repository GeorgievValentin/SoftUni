def shoot(command, targets):
    command = command.split()
    index = int(command[1])
    power = int(command[2])

    if 0 <= index < len(targets):
        targets[index] -= power
        if targets[index] <= 0:
            del targets[index]

    return targets


def add(command, targets):
    command = command.split()
    index = int(command[1])
    value = int(command[2])
    if 0 <= index < len(targets):
        targets.insert(index, value)

        return targets
    print("Invalid placement!")


def strike(command, targets):
    command = command.split()
    index = int(command[1])
    radius = int(command[2])
    if index - radius < 0 or index + radius >= len(targets):
        print("Strike missed!")
    else:
        start_index = index - radius
        end_index = index + radius + 1
        del targets[start_index:end_index]

    return targets


def moving_targets(targets):
    while True:
        command = input()
        if command == "End":
            break

        result = commands[command.split()[0]](command, targets)
    return result


commands = {
    "Shoot": shoot,
    "Add": add,
    "Strike": strike,
}

targets_list = [int(value) for value in input().split()]
targets_ = moving_targets(targets_list)
target_list_string = [str(el) for el in targets_list]
print("|".join(target_list_string))
