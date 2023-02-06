letters = input().split(", ")
result = {letter: ord(letter) for letter in letters}

# for letter in letters:
#     result[letter] = int(ord(letter))
print(result)