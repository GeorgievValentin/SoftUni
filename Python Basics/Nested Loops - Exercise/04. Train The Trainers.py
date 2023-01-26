jury_count = int(input())
theme = input()
theme_count = 0
total_grade = 0
curent_total_grade = 0
while theme != "Finish":
    theme_count += 1
    for i in range(jury_count):
        grade = float(input())
        curent_total_grade += grade
    average_grade = curent_total_grade / jury_count
    total_grade += average_grade
    print(f"{theme} - {average_grade:.2f}.")
    curent_total_grade = 0
    theme = input()
average_total_grade = total_grade / theme_count
print(f"Student's final assessment is {average_total_grade:.2f}.")