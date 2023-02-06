file_path = "./text.txt"

try:
    file = open(file_path, "r")
    print("File found")
except FileNotFoundError:
    print(f"{file_path} does not exist")
