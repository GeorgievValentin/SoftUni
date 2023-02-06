word = input()
unwanted_letters = ["a", "o", "u", "e", "i"]
result = [el for el in word if el not in unwanted_letters]
print("".join(result))
