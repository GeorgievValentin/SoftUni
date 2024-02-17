def print_result(houses_list, current_index):
    print(f"Cupid's last position was {current_index}.")

    if sum(houses_list) == 0:
        print("Mission was successful.")
    else:
        failed_houses = [house for house in houses_list if not house == 0]
        print(f"Cupid has failed {len(failed_houses)} places.")


def hearts_amount(index, houses):
    if houses[index] == 0:
        print(f"Place {index} already had Valentine's day.")
    else:
        houses[index] -= 2
        if houses[index] == 0:
            print(f"Place {index} has Valentine's day.")


def heart_delivery(houses_list):
    current_index = 0

    while True:
        command = input()
        if command == "Love!":
            break

        step = int(command.split()[1])

        if current_index + step > len(houses_list) - 1:
            current_index = 0
            hearts_amount(current_index, houses_list)
        else:
            current_index += step
            hearts_amount(current_index, houses_list)

    return houses_list, current_index


data = [int(num) for num in input().split("@")]
houses_list_, last_index = heart_delivery(data)
print_result(houses_list_, last_index)
