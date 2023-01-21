from math import floor, ceil

area = int(input())
production = float(input())
wine_needed = float(input())
workers = int(input())
kilos_for_liter = 2.5
wine_liters = area / kilos_for_liter * production * 0.4
diff = abs(wine_needed - wine_liters)
liters_per_worker = diff / workers

if wine_needed > wine_liters:
    print(f"It will be a tough winter! More {floor(diff)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(wine_liters)} liters.")
    print(f"{ceil(diff)} liters left -> {ceil(liters_per_worker)} liters per person.")
