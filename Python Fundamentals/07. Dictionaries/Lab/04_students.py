command = input()
courses = {}

while ":" in command:
    data = command.split(":")
    name, id, course = data[0], data[1], data[2]
    if course not in courses:
        courses[course] = {}
    courses[course][id] = name
    command = input()

searched_course = command.replace("_", " ")
for crs, students in courses.items():
    if crs == searched_course:
        for id, name in students.items():
            print(f"{name} - {id}")
