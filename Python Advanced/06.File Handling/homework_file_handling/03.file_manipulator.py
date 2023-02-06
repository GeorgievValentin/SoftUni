import os

command = input()

while not command == "End":
    data = command.split("-")
    action = data[0]
    file_name = data[1]

    if action == "Create":
        file = open(f"../text_files/{file_name}", "w")
        file.close()

    elif action == "Add":
        with open(f"../text_files/{file_name}", "a") as file:
            file.write(f"{data[2]}\n")

    elif action == "Replace":
        try:
            with open(f"../text_files/{file_name}", "r") as file:
                text = file.readlines()

            file = open(f"../text_files/{file_name}", "w")

            for i in range(len(text)):
                text[i] = text[i].replace(data[2], data[3])

            file.write("".join(text))
            file.close()

        except FileNotFoundError:
            print("An error occurred")

    elif action == "Delete":
        try:
            os.remove(f"../text_files/{file_name}")
        except FileNotFoundError:
            print("An error occurred")

    command = input()
