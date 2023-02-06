rows, cols = [int(x) for x in input().split()]
text = input()

matrix = []
index = 0

for i in range(rows):
    row_elements = cols * [None]
    if i % 2 == 0:
        for j in range(cols):
            row_elements[j] = text[index % len(text)]
            index += 1
    else:
        for j in range(cols - 1, -1, -1):
            row_elements[j] = text[index % len(text)]
            index += 1
    print(*row_elements, sep="")
