command = input()
coffee_count = 0
extra_sleep = False

while not command == "END":
    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        coffee_count += 1
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        coffee_count += 2
    if coffee_count > 5:
        extra_sleep = True
    command = input()
if extra_sleep:
    print("You need extra sleep")
else:
    print(coffee_count)
