first_letter = input()
last_letter = input()
exclussive_letter = input()
start_loop = ord(first_letter)
end_loop = ord(last_letter)
counter = 0

for i in range(start_loop, end_loop + 1):
    for j in range(start_loop, end_loop + 1):
        for k in range(start_loop, end_loop + 1):
            if chr(i) != exclussive_letter and chr(j) != exclussive_letter and chr(k) != exclussive_letter:
                counter += 1
                print(f"{chr(i)}{chr(j)}{chr(k)}", end=" ")