loads = int(input())
bus_weight = 0
truck_weight = 0
train_weight = 0
price = 0
total_weight = 0
cost = 0
for i in range(loads):
    weight = int(input())
    total_weight += weight
    if weight <= 3:
        bus_weight += weight
        price = 200
    elif weight <= 11:
        truck_weight += weight
        price = 175
    else:
        train_weight += weight
        price = 120
    cost += weight * price

average_price = cost / total_weight
bus_percent = bus_weight / total_weight * 100
truck_percent = truck_weight / total_weight * 100
train_percent = train_weight / total_weight * 100
print(f"{average_price:.2f}")
print(f"{bus_percent:.2f}%")
print(f"{truck_percent:.2f}%")
print(f"{train_percent:.2f}%")