stack = []
num = int(input())
for _ in range(num):
    command = input()
    if command.startswith("1"):
        numm_to_push = int(command.split()[1])
        stack.append(numm_to_push)
    elif stack:
        if command == "2":
            stack.pop()
        elif command == "3":
            print(max(stack))
        else:
            print(min(stack))
result = [str(el) for el in stack]
print(", ".join(reversed(result)))



