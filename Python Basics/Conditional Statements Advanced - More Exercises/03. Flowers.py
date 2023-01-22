chrysanthemums = int(input())
roses = int(input())
tulips =  int(input())
season = input()
holyday = input()
total_flowers = chrysanthemums + roses + tulips
chrysanthemum_price = 0
rose_price = 0
tulip_price = 0
cost = 0
if season == "Spring" or season == "Summer":
    chrysanthemum_price = 2
    rose_price = 4.1
    tulip_price = 2.5
elif season == "Autumn" or season == "Winter":
    chrysanthemum_price = 3.75
    rose_price = 4.5
    tulip_price = 4.15
cost += chrysanthemum_price * chrysanthemums + rose_price * roses + tulip_price * tulips
if holyday == "Y":
    cost *= 1.15
if tulips > 7 and season == "Spring":
    cost *= 0.95
if roses >= 10 and season == "Winter":
    cost *= 0.9
if total_flowers > 20:
    cost *= 0.8
print(f"{2 + cost:.2f}")