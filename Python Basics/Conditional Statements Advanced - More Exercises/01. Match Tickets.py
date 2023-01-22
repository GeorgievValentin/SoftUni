budget = float(input())
category = input()
people = int(input())
ticket_price = 0
if category == "VIP":
    ticket_price = 499.99
elif category == "Normal":
    ticket_price = 249.99
if people < 5:
    budget *= 0.25
elif people < 10:
    budget *= 0.4
elif people < 25:
    budget *= 0.5
elif people < 50:
    budget *= 0.6
else:
    budget *= 0.75
cost = people * ticket_price
diff = abs(budget - cost)
if budget < cost:
    print(f"Not enough money! You need {diff:.2f} leva.")
else:
    print(f"Yes! You have {diff:.2f} leva left.")