command = input()
products = {}

while not command == "statistics":
    product, value = command.split(": ")
    if product not in products:
        products[product] = int(value)
    else:
        products[product] += int(value)
    command = input()

print("Products in stock:")
for product, value in products.items():
    print(f"- {product}: {value}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
