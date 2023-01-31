from collections import deque

effects = deque(int(x) for x in input().split(", "))
powers = [int(x) for x in input().split(", ")]

fireworks = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}

while effects and powers:
    effect = effects.popleft()
    if effect <= 0:
        continue
    power = powers.pop()
    if power <= 0:
        effects.appendleft(effect)
        continue

    result = effect + power
    if result % 3 == 0 and not result % 5 == 0:
        fireworks["Palm Fireworks"] += 1
    elif result % 5 == 0 and not result % 3 == 0:
        fireworks["Willow Fireworks"] += 1
    elif result % 3 == 0 and result % 5 == 0:
        fireworks["Crossette Fireworks"] += 1
    else:
        effects.append(effect - 1)
        powers.append(power)
    if fireworks["Palm Fireworks"] >= 3 and fireworks["Willow Fireworks"] >= 3 and fireworks["Crossette Fireworks"] >= 3:
        break
if fireworks["Palm Fireworks"] >= 3 and fireworks["Willow Fireworks"] >= 3 and fireworks["Crossette Fireworks"] >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in effects)}")
if powers:
    print(f"Explosive Power left: {', '.join(str(x) for x in powers)}")
for firework, value in fireworks.items():
    print(f"{firework}: {value}")
