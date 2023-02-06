actions = input().split("|")
energy = 100
coins = 100
completed = True
for action in actions:
    action = action.split("-")
    event = action[0]
    number = int(action[1])
    gained_energy = 0
    earned_coins = 0
    if event == "rest":
        gained_energy = min(number, 100 - energy)
        energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event == "order":
        if energy >= 30:
            earned_coins = number
            coins += earned_coins
            energy -= 30
            print(f"You earned {earned_coins} coins.")
        else:
            energy += 50
            print("You had to rest!")
 
    else:

        coins -= number
        if coins >= 0:
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            completed = False
            break
if completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
