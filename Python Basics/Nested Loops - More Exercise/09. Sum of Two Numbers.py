first_num = int(input())
last_num = int(input())
magic_num = int(input())
counter = 0
magic = False

for x in range(first_num, last_num + 1):
    for y in range(first_num, last_num + 1):
        counter += 1
        if x + y == magic_num:
            print(f"Combination N:{counter} ({x} + {y} = {magic_num})")
            magic = True
            break
    if magic:
        break
if not magic:
    print(f"{counter} combinations - neither equals {magic_num}")