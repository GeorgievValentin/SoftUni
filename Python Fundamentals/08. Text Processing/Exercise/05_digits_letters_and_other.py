text = input()
nums = ""
letters = ""
others = ""
for symbol in text:
    if symbol.isdigit():
        nums += symbol
    elif symbol.isalpha():
        letters += symbol
    else:
        others += symbol
print(nums)
print(letters)
print(others)
