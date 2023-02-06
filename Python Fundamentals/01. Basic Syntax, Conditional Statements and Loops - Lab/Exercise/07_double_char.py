word = input()

while not word == "End":
    final = ""
    if not word == "SoftUni":
        for char in word:
            final += char * 2
        print(final)
    word = input()
