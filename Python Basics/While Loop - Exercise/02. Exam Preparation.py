fails_limit = int(input())
name = input()
task = ""
fails = 0
total_score = 0
count = 0
failed = False
while name != "Enough":
    grade = int(input())
    task = name
    count += 1
    total_score += grade
    if grade <= 4:
        fails += 1
    if fails == fails_limit:
        failed = True
        break
    name = input()
if failed:
    print(f"You need a break, {fails} poor grades.")
else:
    average_score = total_score / count
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {count}")
    print(f"Last problem: {task}")