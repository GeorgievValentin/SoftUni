command = input()
counter = 1
resources = {}
resource = ""
quantity = 0
while not command == "stop":
    if not counter % 2 == 0:
        resource = command
        if resource not in resources:
            resources[resource] = 0
    else:
        quantity = int(command)
        resources[resource] += quantity
    counter += 1
    command = input()
for res, value in resources.items():
    print(f"{res} -> {value}")
