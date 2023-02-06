command = input()
contacts = {}
while "-" in command:
    name, number = command.split("-")
    contacts[name] = number
    command = input()
num = int(command)
for i in range(num):
    searched_contact = input()
    if searched_contact in contacts:
        print(f"{searched_contact} -> {contacts[searched_contact]}")
    else:
        print(f"Contact {searched_contact} does not exist.")
