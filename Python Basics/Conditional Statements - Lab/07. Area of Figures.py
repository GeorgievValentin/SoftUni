from math import pi

figure_type = input()
area = 0
if figure_type == "square":
    dimension = float(input())
    area = dimension * dimension
elif figure_type == "rectangle":
    dimension = float(input())
    dimension_2 = float(input())
    area = dimension * dimension_2
elif figure_type == "circle":
    dimension = float(input())
    area = dimension * dimension * pi
elif figure_type == "triangle":
    dimension = float(input())
    dimension_2 = float(input())
    area = dimension * dimension_2 / 2
print(f"{area:.3f}")
