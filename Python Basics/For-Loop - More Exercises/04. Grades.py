students = int(input())
over_5 = 0
over_4 = 0
over_3 = 0
under_3 = 0
total_grade = 0
for i in range(students):
    grade = float(input())
    total_grade += grade
    if grade >= 5:
        over_5 += 1
    elif grade >= 4:
        over_4 += 1
    elif grade >= 3:
        over_3 += 1
    else:
        under_3 += 1

average_grade = total_grade / students
over_5_percent = over_5 / students * 100
over_4_percent = over_4 / students * 100
over_3_percent = over_3 / students * 100
under_3_percent = under_3 / students * 100

print(f"Top students: {over_5_percent:.2f}%")
print(f"Between 4.00 and 4.99: {over_4_percent:.2f}%")
print(f"Between 3.00 and 3.99: {over_3_percent:.2f}%")
print(f"Fail: {under_3_percent:.2f}%")
print(f"Average: {average_grade:.2f}")