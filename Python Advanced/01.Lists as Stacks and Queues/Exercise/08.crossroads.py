# from collections import deque
#
# current_car = ""
# crash = False
# passed_cars = 0
# green_light_duration = int(input())
# free_window = int(input())
# time_to_pass = green_light_duration + free_window
# command = input()
# cars_queue = deque
# while not command == "END":
#     if not command == "green":
#         cars_queue.append(command)
#     else:
#         for el in cars_queue:
#             if time_to_pass >= len(el):
#                 current_car = cars_queue.popleft()
#                 passed_cars += 1
#                 time_to_pass -= len(el)
#             else:
#                 hit_at_index = len(el) - time_to_pass  # check to make it index (-1)
#                 print("A crash happened!")
#                 print(f"{current_car} was hit at {current_car[hit_at_index]}.")
#                 crash = True
#                 break
#     if crash:
#         break
#     command = input()
# print("Everyone is safe.")
# print(f"{passed_cars} total cars passed the crossroads.")

from collections import deque

green_light = int(input())
window = int(input())

cars = deque()
cars_counter = 0
crashed = False

command = input()

while not command != "END":
    if command == "green":
        if cars:
            current = cars.popleft()
            seconds_left = green_light - len(current)
            while seconds_left > 0:
                cars_counter += 1
                if cars:
                    current = cars.popleft()
                    seconds_left -= len(current)
                else:
                    break
            if seconds_left == 0:
                cars_counter += 1
            if window >= abs(seconds_left):
                if seconds_left < 0:
                    cars_counter += 1
            else:
                idx = window + seconds_left
                print("A crash happened!")
                print(f"{current} was hit at {current[idx]}.")
                crashed = True
                break
    else:
        cars.append(command)
    command = input()

if not crashed:
    print("Everyone is safe.")
    print(f"{cars_counter} total cars passed the crossroads.")