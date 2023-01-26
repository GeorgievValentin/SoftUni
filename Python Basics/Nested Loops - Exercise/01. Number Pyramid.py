num = int(input())
counter = 1
finish_printing = False
for row in range(1, num + 1):
    for col in range(1, row + 1):
        print(counter, end=" ")
        counter += 1
        if counter > num:
            finish_printing = True
            break
    if finish_printing:
        break
    print()