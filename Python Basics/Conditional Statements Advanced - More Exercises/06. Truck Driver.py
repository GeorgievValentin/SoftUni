season = input()
montly_kilometers = float(input())
total_kilometers = montly_kilometers * 4
price_km = 0
earn = 0
cost = 0.9
if montly_kilometers <= 5000:
    if season == "Spring" or season == "Autumn":
        price_km = 0.75
    elif season == "Summer":
        price_km = 0.9
    else:
        price_km = 1.05
elif montly_kilometers <= 10000:
    if season == "Spring" or season == "Autumn":
        price_km = 0.95
    elif season == "Summer":
        price_km = 1.1
    else:
        price_km = 1.25
elif montly_kilometers <= 20000:
    price_km = 1.45
earn = total_kilometers * price_km * cost
print(f"{earn:.2f}")