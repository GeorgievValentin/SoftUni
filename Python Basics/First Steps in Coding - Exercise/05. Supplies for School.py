pens = int(input())
markers = int(input())
litres_fluid = int(input())
discount = int(input()) / 100
pen_price = 5.8
marker_price = 7.2
fluid_price = 1.2
total = pens * pen_price + markers * marker_price + litres_fluid * fluid_price
total_sum = total - total * discount
print(total_sum)