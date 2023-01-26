days = int(input())
hours_for_day = int(input())
cost = 0
price = 0
day = 0

for i in range(1 ,days + 1):
    day += 1
    day_cost = 0
    for j in range(1, hours_for_day + 1):
        if i % 2 == 0 and j % 2 != 0:
            price = 2.5
        elif i % 2 != 0 and j % 2 == 0:
            price = 1.25
        else:
            price = 1
        day_cost += price
    cost += day_cost
    print(f"Day: {day} - {day_cost:.2f} leva")
print(f"Total: {cost:.2f} leva")
