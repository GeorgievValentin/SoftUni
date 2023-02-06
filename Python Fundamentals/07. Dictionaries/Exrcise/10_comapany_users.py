command = input()
data = {}
while not command == "End":
    company, user_id = command.split(" -> ")
    if company not in data:
        data[company] = []
    if user_id not in data[company]:
        data[company].append(user_id)
    command = input()


for comp, users in data.items():
    print(f"{comp}")
    for user in users:
        print(f"-- {user}")

