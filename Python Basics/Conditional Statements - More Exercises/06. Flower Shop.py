import math

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cacti = int(input())
gift_price = float(input())
magnolia_price = 3.25
hyacinth_price = 4
rose_price = 3.5
cactus_price = 8

earns = (magnolias * magnolia_price + hyacinths * hyacinth_price + roses * rose_price + cacti * cactus_price) * 0.95
diff = abs(earns - gift_price)
if gift_price > earns:
    print(f"She will have to borrow {math.ceil(diff)} leva.")
else:
    print(f"She is left with {math.floor(diff)} leva.")
