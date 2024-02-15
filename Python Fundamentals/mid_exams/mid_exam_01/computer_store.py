prices = []
customer_type = ""

while True:
    command = input()
    if command in ["special", "regular"]:
        customer_type = command
        break
    if float(command) < 0:
        print("Invalid price!")
        continue
    prices.append(float(command))

taxes_sum = sum(price * 0.2 for price in prices)
cost_wo_taxes = sum(prices)
total_cost = sum(prices) + taxes_sum

if customer_type == "special":
    total_cost *= 0.9

if total_cost == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {cost_wo_taxes:.2f}$\n"
          f"Taxes: {taxes_sum:.2f}$\n"
          "-----------\n"
          f"Total price: {total_cost:.2f}$")
