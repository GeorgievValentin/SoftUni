num = int(input())
data = {}
for i in range(num):
    command = input().split()
    if command[0] == "register":
        username = command[1]
        reg_number = command[2]
        if username not in data:
            data[username] = {"reg_num": reg_number, "action": "register"}
            print(f"{username} registered {reg_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {reg_number}")
    elif command[0] == "unregister":
        username = command[1]
        if username not in data:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            data.pop(username)

for key, value in data.items():
    print(f"{key} => {value['reg_num']}")
