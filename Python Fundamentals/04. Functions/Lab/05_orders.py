def calculates_total_price(product, quantity):
    if product == "coffee":
        return quantity * 1.5
    elif product == "coke":
        return quantity * 1.4
    elif product == "water":
        return quantity
    elif product == "snacks":
        return quantity * 2.00


prod = input()
q = int(input())
result = calculates_total_price(prod, q)
print(f"{result:.2f}")