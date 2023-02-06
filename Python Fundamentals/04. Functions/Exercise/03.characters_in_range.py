def characters_in_range(char1, char2):
    chars = []
    for char in range(ord(char1) + 1, ord(char2)):
        chars.append(chr(char))
    return " ".join(chars)


ch_1 = input()
ch_2 = input()
result = characters_in_range(ch_1, ch_2)
print(result)
