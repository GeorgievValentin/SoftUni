season = input()
group_type = input()
students = int(input())
nights = int(input())
price = 0
sport = ""

if season == "Winter":
    if group_type == "boys":
        price = 9.6
        sport = "Judo"
    elif group_type == "girls":
        price = 9.6
        sport = "Gymnastics"
    else:
        price = 10
        sport = "Ski"
elif season == "Spring":
    if group_type == "boys":
        price = 7.2
        sport = "Tennis"
    elif group_type == "girls":
        price = 7.2
        sport = "Athletics"
    else:
        price = 9.50
        sport = "Cycling"
else:
    if group_type == "boys":
        price = 15
        sport = "Football"
    elif group_type == "girls":
        price = 15
        sport = "Volleyball"
    else:
        price = 20
        sport = "Swimming"
cost = price * students * nights
if students >= 50:
    cost *= 0.50
elif students >= 20:
    cost *= 0.85
elif students >= 10:
    cost *= 0.95
print(f"{sport} {cost:.2f} lv.")