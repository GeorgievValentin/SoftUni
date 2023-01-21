current_record = float(input())
distance = float(input())
time_per_meter = float(input())
slow_down = distance // 15 * 12.5

new_record = distance * time_per_meter + slow_down
diff = abs(current_record - new_record)
if new_record < current_record:
    print(f"Yes, he succeeded! The new world record is {new_record:.2f} seconds.")
else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
    