turns = int(input())
betwen_0_9 = 0
betwen_10_19 = 0
betwen_20_29 = 0
betwen_30_39 = 0
betwen_40_50 = 0
invalid_numbers = 0
points = 0

for i in range(turns):
    number = int(input())
    if 0 <= number <= 9:
        betwen_0_9 += 1
        points += number * 0.2
    elif 10 <= number <= 19:
        betwen_10_19 += 1
        points += number * 0.3
    elif 20 <= number <= 29:
        betwen_20_29 += 1
        points += number * 0.4
    elif 30 <= number <= 39:
        betwen_30_39 += 1
        points += 50
    elif 40 <= number <= 50:
        betwen_40_50 += 1
        points += 100
    else:
        invalid_numbers += 1
        points /= 2

betwen_0_9_percent = betwen_0_9 / turns * 100
betwen_10_19_percent = betwen_10_19 / turns * 100
betwen_20_29_percent = betwen_20_29 / turns * 100
betwen_30_39_percent = betwen_30_39 / turns * 100
betwen_40_50_percent = betwen_40_50 / turns * 100
invalid_numbers_percent = invalid_numbers / turns * 100

print(f"{points:.2f}")
print(f"From 0 to 9: {betwen_0_9_percent:.2f}%")
print(f"From 10 to 19: {betwen_10_19_percent:.2f}%")
print(f"From 20 to 29: {betwen_20_29_percent:.2f}%")
print(f"From 30 to 39: {betwen_30_39_percent:.2f}%")
print(f"From 40 to 50: {betwen_40_50_percent:.2f}%")
print(f"Invalid numbers: {invalid_numbers_percent:.2f}%")
