budget = float(input())
action = input()

while not action == "End":
    budget -= float(action)
    if budget < 0:
        print("You went in overdraft!")
        break
    action = input()
else:
    print("You bought everything needed.")