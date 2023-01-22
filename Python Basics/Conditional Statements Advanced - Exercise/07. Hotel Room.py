month = input()
nights = int(input())
studio = 0
apartament = 0
if month == "May" or month == "October":
    apartament = 65
    studio = 50
    if nights > 14:
        studio *= 0.7
    elif nights > 7:
        studio *= 0.95
elif month == "June" or month == "September":
    apartament = 68.7
    studio = 75.2
    if nights > 14:
        studio *= 0.8
elif month == "July" or month == "August":
    apartament = 77
    studio = 76
if nights > 14:
    apartament *= 0.9
cost_apartament = nights * apartament
cost_studio = nights * studio
print(f"Apartment: {cost_apartament:.2f} lv.")
print(f"Studio: {cost_studio:.2f} lv.")
