budget = float(input())
season = input()
type = ""
location = ""
price = 0

if budget <= 1000:
    type = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.45
elif budget <= 3000:
    type = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.8
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.6
else:
    type = "Hotel"
    if season == "Summer":
        location = "Alaska"
    elif season == "Winter":
        location = "Morocco"
    price = budget * 0.9
print(f"{location} - {type} - {price:.2f}")