target_steps = 10000
steps = 0
while steps < target_steps:
    action = input()
    if action == "Going home":
        steps += int(input())
        break
    else:
        steps += int(action)
diff = abs(target_steps - steps)
if target_steps < steps:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")