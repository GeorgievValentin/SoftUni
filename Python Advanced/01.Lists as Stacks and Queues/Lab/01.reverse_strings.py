text = list(input())
stack = []

while text:
    stack.append(text.pop())
print("".join(stack))

