num = int(input())
cars = set()
for _ in range(num):
    direction, number = input().split(", ")
    if direction == "IN":
        cars.add(number)
    elif direction == "OUT" and cars:
        cars.remove(number)
if cars:
    print("\n".join(cars))
else:
    print("Parking Lot is Empty")
