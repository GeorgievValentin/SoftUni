num = int(input())
valid = (100 <= num <= 200) or num == 0
if not valid:
    print("invalid")
