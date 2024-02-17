def recalculate_values(targets_list: list, index: int):
    current_value = targets_list[index]
    target_values[index] = - 1

    for i in range(len(target_values)):
        if target_values[i] == -1:
            continue
        if targets_list[i] > current_value:
            targets_list[i] -= current_value
        else:
            targets_list[i] += current_value

    return targets_list


def shot_for_the_win(target_list):
    shot_targets = 0

    while True:
        command = input()
        if command == "End":
            break
        index = int(command)
        if index > len(target_list) - 1:
            continue

        shot_targets += 1
        target_list = recalculate_values(target_list, index)

    return shot_targets, target_list


target_values = [int(num) for num in input().split()]
result = shot_for_the_win(target_values)

count_shot_targets, targets = result
targets_as_string = ' '.join(str(num) for num in targets)


print(f"Shot targets: {count_shot_targets} -> {targets_as_string}")
