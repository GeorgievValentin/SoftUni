x = float(input())
y = float(input())
h = float(input())
green_area = x * x * 2 + x * y * 2 - 1.2 * 2 - 1.5 * 1.5 * 2
red_area = x * y * 2 + x * h
green_paint = green_area / 3.4
red_paint = red_area / 4.3
print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")