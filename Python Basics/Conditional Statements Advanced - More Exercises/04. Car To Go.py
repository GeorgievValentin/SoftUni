budget = float(input())
season = input()
type = ""
coupe = ""
price = 0
if budget <= 100:
    type = "Economy class"
    if season == "Summer":
        coupe = "Cabrio"
        price = budget * 0.35
    elif season == "Winter":
        coupe = "Jeep"
        price = budget * 0.65
elif budget <= 500:
    type = "Compact class"
    if season == "Summer":
        coupe = "Cabrio"
        price = budget * 0.45
    elif season == "Winter":
        coupe = "Jeep"
        price = budget * 0.8
else:
    type = "Luxury class"
    coupe = "Jeep"
    price = budget * 0.9
print(f"{type}")
print(f"{coupe} - {price:.2f}")