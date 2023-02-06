command = input()
products = {}
while not command == "buy":
    product, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if product not in products:
        products[product] = {"price": price, "quantity": quantity}
    else:
        products[product]["quantity"] += quantity
        products[product]["price"] = price
    command = input()
for key, value in products.items():
    result = value["price"] * value["quantity"]
    print(f"{key} -> {result:.2f}")

