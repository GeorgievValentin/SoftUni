def valid_indexes(i_1: int, i_2: int, length: int):
    if i_1 == i_2 or i_1 < 0 or i_2 < 0 or i_1 >= length or i_2 >= length:
        return False
    return True


def remove_item(elements: list, item: str):
    elements[:] = [el for el in elements if not el == item]
    return elements


def add_item(elements: list, item: str):
    middle_index = len(elements) // 2

    elements.insert(middle_index, item)
    elements.insert(middle_index + 1, item)

    return elements


def memory_game(elements: list):
    game_won = False  # Initialize game_won to False
    counter = 0
    while True:
        counter += 1
        command = input()
        if command == "end":
            print("Sorry you lose :(\n"
                  f"{' '.join(elements)}")
            break

        indexes = [int(num) for num in command.split()]
        index_1, index_2 = indexes
        if valid_indexes(index_1, index_2, len(elements)):
            if elements[index_1] == elements[index_2]:
                item = elements[index_1]
                remove_item(elements, item)
                print(f"Congrats! You have found matching elements - {item}!")
                if not elements:  # Check if the list is empty
                    game_won = True
                    break
            elif not elements[index_1] == elements[index_2]:
                print("Try again!")
        else:
            item_to_add = f"-{counter}a"
            add_item(elements, item_to_add)
            print("Invalid input! Adding additional elements to the board")

    if game_won:
        print(f"You have won in {counter} turns!")


elements_ = input().split()
memory_game(elements_)
