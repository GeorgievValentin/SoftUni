num = int(input())
students = {}
for _ in range(num):
    student = input()
    grade = float(input())
    if student not in students:
        students[student] = []
    students[student].append(grade)
for stud, grades in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.5:
        print(f"{stud} -> {average_grade:.2f}")
