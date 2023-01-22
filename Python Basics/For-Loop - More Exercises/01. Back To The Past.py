money = float(input())
final_year = int(input())
age = 18
for i in range(1800, final_year + 1):
    if i % 2 == 0:
        money -= 12000
    else:
        money -= 12000 + 50 * age
    age += 1
if money < 0:
    print(f"He will need {abs(money):.2f} dollars to survive.")
else:
    print(f"Yes! He will live a carefree life and will have {money:.2f} dollars left.")