capacity = 255
num = int(input())

for pours in range(num):
    liters = int(input())
    if capacity >= liters:
        capacity -= liters
    else:
        print("Insufficient capacity!")
        continue
total = 255 - capacity
print(total)