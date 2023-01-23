change = float(input())
change = int(change * 100)
coins = 0

coins += change // 200
change %= 200
coins += change // 100
change %= 100
coins += change // 50
change %= 50
coins += change // 20
change %= 20
coins += change // 10
change %= 10
coins += change // 5
change %= 5
coins += change // 2
change %= 2
if change == 1:
    coins += 1
print(coins)