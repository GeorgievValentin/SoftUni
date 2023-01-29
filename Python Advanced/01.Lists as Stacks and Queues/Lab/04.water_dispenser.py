from collections import deque

liters = int(input())
name = input()
queue_of_people = deque()

while not name == "Start":
    queue_of_people.append(name)
    name = input()

command = input()
while not command == "End":
    if command.startswith("refill"):
        liters += int(command.split()[-1])
    else:
        wanted_liters = int(command)
        if liters >= wanted_liters:
            liters -= wanted_liters
            print(f"{queue_of_people.popleft()} got water")
        else:
            print(f"{queue_of_people.popleft()} must wait")
    command = input()
print(f"{liters} liters left")
