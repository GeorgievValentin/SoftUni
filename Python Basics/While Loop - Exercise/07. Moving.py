x = int(input())
y = int(input())
z = int(input())
free_space = x * y * z

action = input()
while action != "Done":
    free_space -= int(action)
    if free_space < 0:
        break
    action = input()
if free_space > 0:
    print(f"{free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")