exam_hour = int(input())
exam_minutes = int(input())
arrive_hour = int(input())
arrive_minutes = int(input())
exam_time = exam_hour * 60 + exam_minutes
arrive_time = arrive_hour * 60 + arrive_minutes
diff = abs(exam_time - arrive_time)
if arrive_time > exam_time:
    print("Late")
    if diff > 59:
        print(f"{diff // 60}:{(diff % 60):02d} hours after the start")
    else:
        print(f"{diff} minutes after the start")
elif exam_time - 30 <= arrive_time:
    print("On time")
    if arrive_time < exam_time:
        print(f"{diff} minutes before the start")
else:
    print("Early")
    if diff > 59:
        print(f"{diff // 60}:{(diff % 60):02d} hours before the start")
    else:
        print(f"{diff} minutes before the start")