number = int(input())

all_even = True
for num in range(number):
    current_num = int(input())
    if not current_num % 2 == 0:
        print(f"{current_num} is odd!")
        all_even = False
        break
if all_even:
    print("All numbers are even.")