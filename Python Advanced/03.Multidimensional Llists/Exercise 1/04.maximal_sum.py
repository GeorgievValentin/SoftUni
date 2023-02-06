rows, cols = [int(x) for x in input().split()]

matrix = []
sub_matrix = []
for _ in range(rows):
    nums = [int(x) for x in input().split()]
    matrix.append(nums)
result = -999999999
for i in range(rows - 2):
    for j in range(cols - 2):
        current_result = 0
        current_matrix = (matrix[i][j:j + 3], matrix[i + 1][j:j + 3], matrix[i + 2][j:j + 3])
        for el in current_matrix:
            current_result += sum(el)
        if current_result > result:
            result = current_result
            sub_matrix = current_matrix
print(f"Sum = {result}")
for el in sub_matrix:
    print(" ".join(str(x) for x in el))
