wagons_count = int(input())
list_wagons = [0] * wagons_count
command = input()
while not command == "End":
    command = command.split()
    action = command[0]
    if action == "add":
        people = int(command[1])
        list_wagons[-1] += people
    elif action == "insert":
        index = int(command[1])
        people = int(command[2])
        list_wagons[index] += people
    elif action == "leave":
        index = int(command[1])
        people = int(command[2])
        list_wagons[index] -= people
    command = input()
print(list_wagons)
