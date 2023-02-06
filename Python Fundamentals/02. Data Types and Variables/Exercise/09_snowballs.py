num = int(input())
weight = 0
time = 0
quality = 0
value = 0
for ball in range(num):
    current_weight = int(input())
    current_time = int(input())
    current_quality = int(input())
    current_value = (current_weight / current_time) ** current_quality
    if current_value > value:
        value = current_value
        weight = current_weight
        time = current_time
        quality = current_quality
print(f"{weight} : {time} = {int(value)} ({quality})")