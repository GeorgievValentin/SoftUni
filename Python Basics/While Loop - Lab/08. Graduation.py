name = input()
fails = 0
year = 1
total_grade = 0
excluded = False
while year <= 12:
    grade = float(input())
    if grade < 4:
        fails += 1
        if fails > 1:
            excluded = True
            break
    else:
        year += 1
        total_grade += grade
average_grade = total_grade / 12
if excluded:
    print(f"{name} has been excluded at {year} grade")
else:
    print(f"{name} graduated. Average grade: {average_grade:.2f}")