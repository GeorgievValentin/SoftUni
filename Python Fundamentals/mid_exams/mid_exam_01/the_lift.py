def print_result(people_count: int, wagons: list):
    wagons_as_string = [str(wagon) for wagon in wagons]
    if not people_count and not wagons[-1] == 4:
        result = ("The lift has empty spots!\n"
                  f"{' '.join(wagons_as_string)}")
    elif people_count and wagons[-1] == 4:
        result = (f"There isn't enough space! {people_count} people in a queue!\n"
                  f"{' '.join(wagons_as_string)}")
    else:
        result = f"{' '.join(wagons_as_string)}"

    return result


def the_lift(people_count: int, wagons: list):
    wagon_capacity = 4
    for i in range(len(wagons)):
        if wagons[i] < wagon_capacity:
            if people_count < wagon_capacity:
                wagons[i] += people_count
                people_count = 0
            else:
                people_count -= wagon_capacity - wagons[i]
                wagons[i] = wagon_capacity
        if people_count == 0:
            break
    return print_result(people_count, wagons)


people_queue = int(input())
wagon_sequence = [int(wagon) for wagon in input().split()]

print(the_lift(people_queue, wagon_sequence))

