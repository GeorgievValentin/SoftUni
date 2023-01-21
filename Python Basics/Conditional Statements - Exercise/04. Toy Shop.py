trip_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

puzzle_price = 2.6
doll_price = 3
bear_price = 4.1
minion_price = 8.2
truck_price = 2
toys = puzzles + dolls + bears + minions + trucks
earn = puzzles * puzzle_price + dolls * doll_price + bears * bear_price + minions * minion_price + trucks * truck_price
if toys >= 50:
    earn *= 0.75
earn *= 0.9
difference = abs(earn - trip_price)
if earn >= trip_price:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")