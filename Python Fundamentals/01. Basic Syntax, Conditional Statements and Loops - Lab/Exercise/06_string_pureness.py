num = int(input())

for i in range(num):
    pure = True
    text = input()
    for char in text:
        if char == "," or char == "." or char == "_":
            pure = False
    if pure:
        print(f"{text} is pure.")
    else:
        print(f"{text} is not pure!")
