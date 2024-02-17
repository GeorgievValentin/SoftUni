def urgent(products_list, item):
    if item not in products_list:
        products_list.insert(0, item)

    return products_list


def unnecessary(products_list, item):
    if item in products_list:
        products_list.remove(item)

    return products_list


def correct(products_list, old_item, new_item):
    if old_item in products_list:
        index = products_list.index(old_item)
        products_list[index] = new_item

    return products_list


def rearrange(products_list, item):
    if item in products_list:
        products_list.remove(item)
        products_list.append(item)

    return products_list


def shopping_list(products_list):
    while True:
        command = input()
        if command == "Go Shopping!":
            break
        command = command.split()
        action = command[0]
        item = command[1]
        if len(command) == 3:
            new_item = command[2]
            products_list = actions[action](products_list, item, new_item)
        else:
            products_list = actions[action](products_list, item)

    return products_list


actions = {
    "Urgent": urgent,
    "Unnecessary": unnecessary,
    "Correct": correct,
    "Rearrange": rearrange,
}

products = input().split("!")
print(", ".join(shopping_list(products)))


# def urgent(products_list, item):
#     if item not in products_list:
#         products_list.insert(0, item)
#     return products_list
#
#
# def unnecessary(products_list, item):
#     if item in products_list:
#         products_list.remove(item)
#     return products_list
#
#
# def correct(products_list, old_item, new_item):
#     if old_item in products_list:
#         index = products_list.index(old_item)
#         products_list[index] = new_item
#     return products_list
#
#
# def rearrange(products_list, item):
#     if item in products_list:
#         products_list.remove(item)
#         products_list.append(item)  # Append it to the end of the list
#     return products_list  # Don't forget to return the modified list
#
#
# def shopping_list(products_list):
#     while True:
#         command = input()
#         if command == "Go Shopping!":
#             break
#         command = command.split()
#         action = command[0]
#         item = command[1]
#         if len(command) == 3:
#             new_item = command[2]
#             products_list = actions[action](products_list, item, new_item)
#         else:
#             products_list = actions[action](products_list, item)
#     return products_list
#
#
# actions = {
#     "Urgent": urgent,
#     "Unnecessary": unnecessary,
#     "Correct": correct,
#     "Rearrange": rearrange,
# }
#
# products = input().split("!")
# print(", ".join(shopping_list(products)))
