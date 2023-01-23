book = input()
current_book = input()
found = True
count = 0
while book != current_book:
    current_book = input()
    count += 1
    if current_book == "No More Books":
        found = False
        print(f"The book you search is not here!")
        print(f"You checked {count} books.")
        break
if found:
    print(f"You checked {count} books and found it.")