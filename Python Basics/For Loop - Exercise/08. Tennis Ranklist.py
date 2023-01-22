from math import floor


tournaments = int(input())
points = int(input())
total_points = 0
stage = ""
wins = 0

for i in range(tournaments):
    stage = input()
    if stage == "W":
        wins += 1
        total_points += 2000
    elif stage == "F":
        total_points += 1200
    elif stage == "SF":
        total_points += 720

average_points = total_points / tournaments
total_points = points + total_points
wins_percent = wins / tournaments * 100

print(f"Final points: {total_points}")
print(f"Average points: {floor(average_points)}")
print(f"{wins_percent:.2f}%")