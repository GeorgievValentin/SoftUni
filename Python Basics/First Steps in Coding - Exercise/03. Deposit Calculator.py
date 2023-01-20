deposited_money = float(input())
period = int(input())
interest = float(input())
total = deposited_money + period * deposited_money * interest / 100 / 12
print(total)