mackerel_price = float(input())
toy_price = float(input())
bonito_weight = float(input())
horse_weight = float(input())
shell_weight = int(input())

bonito_price = mackerel_price * 1.6
horse_price = toy_price * 1.8
shell_price = 7.5

costs = bonito_weight * bonito_price + horse_weight * horse_price + shell_weight * shell_price

print(f"{costs: .2f}")