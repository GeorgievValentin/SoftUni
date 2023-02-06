n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

main_diagonal = []
secondary_diagonal = []

for i in range(n):
    main_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][n - 1 - i])

diff = abs(sum(main_diagonal) - sum(secondary_diagonal))
print(diff)