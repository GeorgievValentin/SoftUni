text = input()
letters = {}
for letter in text:
    if letter not in letters:
        letters[letter] = 1
    else:
        letters[letter] += 1
for let, value in letters.items():
    if not let == " ":
        print(f"{let} -> {value}")
