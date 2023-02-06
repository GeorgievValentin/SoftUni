from string import punctuation

with open("../text_files/01.text.txt", "r") as text_file:
    text = text_file.readlines()

output_file = open("../text_files/output.txt", "a")

for i in range(len(text)):
    line = text[i]

    letters = 0
    marks = 0

    for el in line:
        if el.isalpha():
            letters += 1
        elif el in punctuation:
            marks += 1

    output_file.write(f"Line {i + 1}: {''.join(line[:-1])} ({letters}) ({marks})\n")

output_file.close()