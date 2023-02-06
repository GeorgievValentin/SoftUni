elements = input().split()
bakery = {}

for index in range(0, len(elements), 2):
    product = elements[index]
    quantity = elements[index + 1]
    bakery[product] = int(quantity)

print(bakery)
