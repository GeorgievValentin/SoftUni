actor_name = input()
points = float(input())
jury_count = int(input())

for i in range(jury_count):
    jury_name = input()
    curent_points = float(input())
    points += len(jury_name) * curent_points / 2
    if points > 1250.5:
        break
diff = 1250.5 - points
if points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")