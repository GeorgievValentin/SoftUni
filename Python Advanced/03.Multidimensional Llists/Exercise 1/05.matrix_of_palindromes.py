rows, cols = [int(x) for x in input().split()]

for i in range(rows):
    for j in range(cols):
        print(f"{chr(97 + i)}{chr(97 + i + j)}{chr(97 + i)}", end=" ")
    print()
