nilon = int(input()) + 2
paint = int(input()) * 1.1
aceton = int(input())
hours = int(input())
nilon_price = 1.5
paint_price = 14.5
aceton_price = 5
bags = 0.4
materials_cost = nilon * nilon_price + paint * paint_price + aceton * aceton_price + bags
workers_cost = materials_cost * 0.3 * hours
total_cost = materials_cost + workers_cost
print(total_cost)