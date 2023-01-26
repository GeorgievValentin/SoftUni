income = 0
while True:
    destination = input()
    if destination == "End":
        break
    cost = float(input())
    while True:
        income += float(input())
        if income >= cost:
            print(f"Going to {destination}!")
            income = 0
            break