chicken_menus = int(input())
fish_menus = int(input())
vege_menus = int(input())
chicken_price = 10.35
fish_price = 12.4
vege_price = 8.15
delivery = 2.5
cost = chicken_menus * chicken_price + fish_menus * fish_price + vege_menus * vege_price
desert = cost * 0.2
total_cost = cost + desert + delivery
print(total_cost)