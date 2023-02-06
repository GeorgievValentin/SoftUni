from os import remove

try:
    remove("my_first_file.txt")
except FileNotFoundError:
    print(f"File already deleted!")
