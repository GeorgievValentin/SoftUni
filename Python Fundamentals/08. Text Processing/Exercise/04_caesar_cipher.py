# text = input()
new_text = "".join([chr(ord(symbol) + 3) for symbol in input()])
print(new_text)
