n = int(input())
matrix = []

for _ in range(n):
    symbols = list(input())
    matrix.append(symbols)
searched_symbol = input()
result = None
for i in range(n):
    for j in range(n):
        if searched_symbol == matrix[i][j]:
            result = (i, j)
            print(result)
            break
    if result:
        break
if not result:
    print(f"{searched_symbol} does not occur in the matrix")

