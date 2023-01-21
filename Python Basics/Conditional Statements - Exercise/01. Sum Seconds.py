time_1 = int(input())
time_2 = int(input())
time_3 = int(input())
total_time = time_1 + time_2 + time_3
minutes = total_time // 60
seconds = total_time % 60
print(f"{minutes}:{seconds:02d}")