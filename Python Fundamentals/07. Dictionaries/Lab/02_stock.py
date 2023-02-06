elements = input().split()
searched_products = input().split()
products = {}

for index in range(0, len(elements), 2):
    product = elements[index]
    value = elements[index + 1]
    products[product] = int(value)

for ser_product in searched_products:
    if ser_product in products:
        print(f"We have {products[ser_product]} of {ser_product} left")
    else:
        print(f"Sorry, we don't have {ser_product}")
