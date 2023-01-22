projection = input()
rows = int(input())
columns = int(input())
price = 0
places = rows * columns

if projection == "Premiere":
    price = 12
elif projection == "Normal":
    price = 7.5
elif projection == "Discount":
    price = 5
earns = price * places

print(f"{earns:.2f} leva")