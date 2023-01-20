area = float(input())
price = 7.61
costs = area * price
total_costs = costs * 0.82
discount = costs - total_costs
print(f"The final price is: {total_costs:.2f} lv.")
print(f"The discount is: {discount:.2f} lv.")