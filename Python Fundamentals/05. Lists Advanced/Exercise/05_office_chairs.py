rooms = int(input())
free_chairs = 0
game_on = True
for num in range(1, rooms + 1):
    chairs, people = input().split()
    diff = abs(len(chairs) - int(people))
    if len(chairs) < int(people):
        print(f"{diff} more chairs needed in room {num}")
        game_on = False
    else:
        free_chairs += diff
if game_on:
    print(f"Game On, {free_chairs} free chairs left")
