command = input()
sides = {}
while not command == "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        if force_side not in sides:
            sides[force_side] = []
        if any(force_user in value for value in sides.values()) is False:
            sides[force_side].append(force_user)
    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        if force_side not in sides:
            sides[force_side] = []
        if any(force_user in value for value in sides.values()) is False:
            sides[force_side].append(force_user)
        else:
            sides[force_side] = force_user
        print(f"{force_user} joins the {force_side} side!")
    command = input()
for key, value in sides.items():
    print(f"Side: {key}, Members: {len(key)}")
