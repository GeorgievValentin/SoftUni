hours = int(input())
minutes = int(input())
time = hours * 60 + minutes + 15
new_hours = time // 60
new_minutes = time % 60
if new_hours >= 24:
    new_hours %= 24
print(f"{new_hours}:{new_minutes:02d}")