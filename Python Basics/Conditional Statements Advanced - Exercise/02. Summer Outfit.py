degreece = int(input())
day_time = input()
outfit = ""
shoes = ""
if day_time == "Morning":
    if 10 <= degreece <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif degreece <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif degreece >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"
elif day_time == "Afternoon":
    if 10 <= degreece <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif degreece <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif degreece >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"
if day_time == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"
print(f"It's {degreece} degrees, get your {outfit} and {shoes}.")