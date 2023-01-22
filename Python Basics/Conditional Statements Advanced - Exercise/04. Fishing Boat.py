budget = int(input())
season = input()
fishers = int(input())
price = 0

if season == "Spring":
    price = 3000
elif season == "Autumn" or season == "Summer":
    price = 4200
elif season == "Winter":
    price = 2600
if fishers <= 6:
    price *= 0.9
elif fishers <= 11:
    price *= 0.85
else:
    price *= 0.75
if fishers % 2 == 0 and season != "Autumn":
    price *= 0.95

diff = abs(budget - price)
if budget >= price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")