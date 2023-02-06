symbols = ["-", ",", ".", "!", "?"]

with open("../text_files/01.text.txt", "r") as even_line_file:
    text = even_line_file.readlines()

for line in range(0, len(text), 2):
    for el in symbols:
        text[line] = text[line].replace(el, "@")

    print(*text[line].split()[::-1], sep=" ")
