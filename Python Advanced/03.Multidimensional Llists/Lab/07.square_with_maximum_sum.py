rows, cols = [int(x) for x in input().split(", ")]
matrix = []
sum_matrix = -999999999999
sub_matrix = []
for _ in range(rows):
    nums = [int(x) for x in input().split(", ")]
    matrix.append(nums)

for i in range(rows - 1):
    for j in range(cols - 1):
        current_sub_matrix = (matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1])
        current_sum_matrix = sum(current_sub_matrix)
        if current_sum_matrix > sum_matrix:
            sum_matrix = current_sum_matrix
            sub_matrix = current_sub_matrix

print(f"{sub_matrix[0]} {sub_matrix[1]}")
print(f"{sub_matrix[2]} {sub_matrix[3]}")
print(sum_matrix)

