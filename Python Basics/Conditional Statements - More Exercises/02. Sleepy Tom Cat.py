non_work_days = int(input())
work_days = 365 - non_work_days
play_norm_minutes = 30000
play_time = non_work_days * 127 + work_days * 63
diff = abs(play_norm_minutes - play_time)

if play_time > play_norm_minutes:
    print("Tom will run away")
    print(f"{diff // 60} hours and {diff % 60} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{diff // 60} hours and {diff % 60} minutes less for play")