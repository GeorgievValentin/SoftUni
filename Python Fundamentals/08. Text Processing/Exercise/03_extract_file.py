file_directory = input().split("\\")
name, extension = file_directory[-1].split(".")
print(f"File name: {name}")
print(f"File extension: {extension}")
