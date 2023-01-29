expression = input()
opening_brackets_stack = []
correct = True
for el in expression:
    if el in "({[":
        opening_brackets_stack.append(el)
    elif el in ")}]":
        closing_bracket = el
        if not opening_brackets_stack:
            correct = False
            break
        opening_bracket = opening_brackets_stack.pop()  # check if in [opening_bracket_stack] are elements
        if f"{opening_bracket}{closing_bracket}" not in "() {} []":
            correct = False
            break

if correct and not opening_brackets_stack:  # no element left in the stack
    print("YES")
else:
    print("NO")