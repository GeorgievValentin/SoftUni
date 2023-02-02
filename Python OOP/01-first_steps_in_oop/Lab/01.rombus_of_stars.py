def print_line(n):
    print((num - row) * " ", end="")
    print(row * "* ")


num = int(input())

for row in range(1, num + 1):
    print_line(num)

for row in range(num - 1, 0, -1):
    print_line(num)