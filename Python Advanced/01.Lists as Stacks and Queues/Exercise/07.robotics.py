from collections import deque


def convert_str_time_to_sec(str_time):
    hours, minutes, seconds = [int(x) for x in str_time.split(":")]
    return hours * 60 * 60 + minutes * 60 + seconds  # add 1 second after the starting hour


def format_seconds(seconds):
    seconds %= 24 * 60 * 60
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


robots_data = input().split(";")
robot_time_processing = {}
robot_time_busy = {}
for robot in robots_data:
    name, processing_time = robot.split("-")
    robot_time_processing[name] = int(processing_time)
    robot_time_busy[name] = -1

time = convert_str_time_to_sec(input())

detail = input()
details_queue = deque()
while not detail == "End":
    details_queue.append(detail)
    detail = input()

while details_queue:
    time += 1
    current_detail = details_queue.popleft()

    for name, busy_until in robot_time_busy.items():
        if time >= busy_until:
            robot_time_busy[name] = time + robot_time_processing[name]
            print(f"{name} - {current_detail} [{format_seconds(time)}]")
            break
    else:
        details_queue.append(current_detail)
