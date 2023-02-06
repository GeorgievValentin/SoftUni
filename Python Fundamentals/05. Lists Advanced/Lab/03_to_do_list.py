command = input()
tasks = [0] * 10
while not command == "End":
    priority, task = command.split("-")
    priority = int(priority) - 1
    # tasks.pop(priority)
    # tasks.insert(priority, task)
    tasks[priority] = task
    command = input()
result = [el for el in tasks if not el == 0]
print(result)
