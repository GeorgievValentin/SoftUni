trip = float(input())
money = float(input())
spend_days = 0
total_days = 0
travel = True
while trip > money:
    total_days += 1
    operation = input()
    curent_money = float(input())
    if operation == "spend":
        money -= curent_money
        spend_days += 1
        if money < curent_money:
            money = 0
        if spend_days == 5:
            travel = False
            break
        continue
    money += curent_money
    spend_days = 0
if travel:
    print(f"You saved the money for {total_days} days.")
else:
    print("You can't save the money.")
    print(f"{total_days}")