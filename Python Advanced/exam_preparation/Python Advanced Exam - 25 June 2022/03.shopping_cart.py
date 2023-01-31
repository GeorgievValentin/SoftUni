def shopping_cart(*args):
    meals = {"Soup": [], "Pizza": [], "Dessert": []}
    result = ""
    for el in args:

        meals_name = el[0]
        product = el[1]

        if el == "Stop":
            break

        if meals_name == "Soup" and len(meals[meals_name]) < 3 and product not in meals[meals_name]:
            meals[meals_name].append(product)
        elif meals_name == "Pizza" and len(meals[meals_name]) < 4 and product not in meals[meals_name]:
            meals[meals_name].append(product)
        elif meals_name == "Dessert" and len(meals[meals_name]) < 2 and product not in meals[meals_name]:
            meals[meals_name].append(product)
    for value in meals.values():
        if len(value) > 0:
            break
    else:
        return 'No products in the cart!'

    sorted_meals = sorted(meals.items(), key=lambda x: (-len(x[1]), x[0]))

    for el in sorted_meals:
        result += f"{el[0]}:\n"
        sorted_product = sorted(el[1])
        for product in sorted_product:
            result += f" - {product}\n"

    return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    ('Dessert', 'milk'),
    ('Soup', 'carrots'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
