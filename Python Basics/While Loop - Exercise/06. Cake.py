a = int(input())
b = int(input())
count = a * b
action = input()
enough = True
while action != "STOP":
    count -= int(action)
    if count < 0:
        enough = False
        break
    action = input()
if enough:
    print(f"{count} pieces are left.")
else:
    print(f"No more cake left! You need {abs(count)} pieces more.")
