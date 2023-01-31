def shopping_list(budget, **kwargs):
    result = ""
    basket = {}
    if budget < 100:
        return "You do not have enough budget."

    for product, (price, quantity) in kwargs.items():
        current_price = price * quantity
        if budget >= current_price and product not in basket:
            basket[product] = current_price
            budget -= current_price
            if len(basket) >= 5:
                break
    for prod, total_price in basket.items():
        result += f"You bought {prod} for {total_price:.2f} leva.\n"

    return result


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
