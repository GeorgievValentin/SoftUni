budget = float(input())
season = input()
type = ""
destination = ""
cost = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        type = "Camp"
        cost = budget * 0.3
    elif season == "winter":
        type = "Hotel"
        cost = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        type = "Camp"
        cost = budget * 0.4
    elif season == "winter":
        type = "Hotel"
        cost = budget * 0.8
elif budget > 1000:
    type = "Hotel"
    destination = "Europe"
    cost = budget * 0.9
print(f"Somewhere in {destination}")
print(f"{type} - {cost:.2f}")