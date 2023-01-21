length = float(input())
width = float(input()) - 1
length_count = length // 1.2
width_count = width // 0.7
places = length_count * width_count - 3
print(int(places))