gifts = input().split()
command = input()

while not command == "No Money":
    current_command = command.split()
    if current_command[0] == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == current_command[1]:
                gifts[i] = "None"
    elif current_command[0] == "Required":
        index = int(current_command[2])
        if 0 <= index < len(gifts):
            gifts[index] = current_command[1]
    elif current_command[0] == "JustInCase":
        gifts[-1] = current_command[1]
    command = input()
for gift in gifts:
    if not gift == "None":
        print(gift, end=" ")
