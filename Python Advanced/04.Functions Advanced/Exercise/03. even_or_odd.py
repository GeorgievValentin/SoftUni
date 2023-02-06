def even_odd(*args):
    nums = list(args)
    command = nums.pop()
    result = []

    if command == "even":
        result = [el for el in nums if el % 2 == 0]

    elif command == "odd":
        result = [el for el in nums if not el % 2 == 0]

    return result


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
