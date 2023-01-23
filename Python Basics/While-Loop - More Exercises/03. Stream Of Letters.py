message = ""
word = ""
c = 0
o = 0
n = 0

while True:
    letter = input()
    if letter == "End":
        break
    if chr(65) <= letter <= chr(90) or chr(97) <= letter <= chr(122):
        if letter == "c" and c == 0:
            c += 1
        elif letter == "o" and o == 0:
            o += 1
        elif letter == "n" and n == 0:
            n += 1
        else:
            word += letter
        if c + o + n == 3:
            word += " "
            message += word
            word = ""
            c = 0
            o = 0
            n = 0
print(message)