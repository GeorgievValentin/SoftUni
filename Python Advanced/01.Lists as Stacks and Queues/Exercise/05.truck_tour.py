from collections import deque

pumps_count = int(input())
data_queue = deque()
pass_the_trip = False

for _ in range(pumps_count):
    pump_data = input().split()
    data_queue.append([int(pump_data[0]), int(pump_data[1])])

for index in range(len(data_queue)):
    passed_pumps = 0
    tank = 0
    for pump in data_queue:
        liters, distance = pump[0], pump[1]
        tank += liters
        if tank < distance:
            break
        tank -= distance
        passed_pumps += 1
        if passed_pumps == pumps_count:
            pass_the_trip = True
    if pass_the_trip:
        print(index)
        break
    data_queue.rotate(-1)

# from collections import deque
#
# petrol_pumps = int(input())
# data_queue = deque()
# trip_passed = False
#
# for _ in range(petrol_pumps):
#     pump_data = input().split()
#     data_queue.append((int(pump_data[0]), int(pump_data[1])))
#
# for index in range(len(data_queue)):
#     passed_pumps = 0
#     tank_liters = 0
#
#     for pump in data_queue:
#         liters, distance = pump[0], pump[1]
#         tank_liters += liters
#         if tank_liters < distance:
#             break
#         tank_liters -= distance
#         passed_pumps += 1
#         if passed_pumps == petrol_pumps:
#             trip_passed = True
#     if trip_passed:
#         print(index)
#         break
#     data_queue.rotate(-1)
#
