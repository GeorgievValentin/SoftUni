employees_happiness = [int(num) for num in input().split()]
factor = int(input())
average_happiness = sum(employees_happiness) * factor / len(employees_happiness)
happy_employees = [num * factor for num in employees_happiness if factor * num >= average_happiness]
if len(happy_employees) >= len(employees_happiness) / 2:
    print(f"Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are not happy!")

