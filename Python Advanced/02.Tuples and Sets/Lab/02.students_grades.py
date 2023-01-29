num = int(input())
data = {}
for _ in range(num):
    name, grade = input().split()
    # grade = float(grade)
    if name not in data:
        data[name] = []
    data[name].append(float(grade))  # or in line 5 make it to float()

for student in data.items():  # with only the tuple(students), not key, value way can do more manipulations on the items
    print(f"{student[0]} -> {' '.join([f'{el:.2f}' for el in student[1]])} (avg: {(sum(student[1])/len(student[1])):.2f})")
print(type(student))  # tuple !!!