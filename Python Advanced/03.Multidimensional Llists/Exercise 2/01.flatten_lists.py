line = input().split("|")
for el in reversed(line):
    symbols = el.split()
    if symbols:
        print(*symbols, end=" ")