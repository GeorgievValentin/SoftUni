usernames = input().split(", ")
valid = False
for name in usernames:
    if 3 < len(name) <= 16 and (name.isalnum() or "-" in name or "_" in name):
        print(name)
