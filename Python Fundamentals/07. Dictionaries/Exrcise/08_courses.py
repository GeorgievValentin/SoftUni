command = input()
data = {}
while not command == "end":
    course, student = command.split(" : ")
    if course not in data:
        data[course] = []
        data[course].append(student)
    else:
        data[course].append(student)
    command = input()
for course_name, students in data.items():
    print(f"{course_name}: {len(students)}")
    for el in students:
        print(f"-- {el}")
