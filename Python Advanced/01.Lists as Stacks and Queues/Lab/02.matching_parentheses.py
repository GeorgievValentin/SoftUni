text = input()
stack_brackets_indexes = []

for index in range(len(text)):
    if text[index] == "(":
        stack_brackets_indexes.append(index)
    elif text[index] == ")":
        starting_index = stack_brackets_indexes.pop()
        print(text[starting_index: index + 1])
