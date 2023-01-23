expected_sum = int(input())

count_cash = 0
count_card = 0
total_cash = 0
total_card = 0
product_count = 0
get_money = False
while True:
    if total_cash + total_card >= expected_sum:
        get_money = True
        break
    command = input()
    if command == "End":
        break
    price = int(command)
    product_count += 1
    cash_payment = product_count % 2 == 1
    if price <= 100 and cash_payment:
        total_cash += price
        count_cash += 1
    elif price >= 10 and not cash_payment:
        total_card += price
        count_card += 1
    else:
        print("Error in transaction!")
        continue
    print("Product sold!")
if get_money:
    print(f"Average CS: {total_cash / count_cash:.2f}")
    print(f"Average CC: {total_card / count_card:.2f}")
else:
    print("Failed to collect required money for charity.")