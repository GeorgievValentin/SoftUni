score = int(input())
bonus = 0
if score <= 100:
    bonus += 5
elif score <= 1000:
    bonus += score * 0.2
else:
    bonus += score * 0.1
if score % 2 == 0:
    bonus += 1
elif score % 10 == 5:
    bonus += 2
total_score = score + bonus
print(bonus)
print(total_score)