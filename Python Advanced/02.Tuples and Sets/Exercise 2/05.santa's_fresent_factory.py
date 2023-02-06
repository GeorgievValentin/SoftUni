from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])
presents = {}
have_presents = False

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    total_magic = current_material * current_magic

    if total_magic == 150:
        if "Doll" not in presents:
            presents["Doll"] = 0
        presents["Doll"] += 1
    elif total_magic == 250:
        if "Wooden train" not in presents:
            presents["Wooden train"] = 0
        presents["Wooden train"] += 1
    elif total_magic == 300:
        if "Teddy bear" not in presents:
            presents["Teddy bear"] = 0
        presents["Teddy bear"] += 1
    elif total_magic == 400:
        if "Bicycle" not in presents:
            presents["Bicycle"] = 0
        presents["Bicycle"] += 1
    elif total_magic > 0:
        materials.append(current_material + 15)
    elif total_magic < 0:
        materials.append(current_material + current_magic)
    else:
        if current_material == 0 and current_magic == 0:
            continue
        elif current_material == 0:
            magic.appendleft(current_magic)
        elif current_magic == 0:
            materials.append(current_material)
    if "Doll" in presents and "Train" in presents:
        have_presents = True
    elif "Teddy bear" in presents and "Bicycle" in presents:
        have_presents = True

if have_presents:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    materials = reversed(materials)
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")
for present, quantity in sorted(presents.items()):
    print(f"{present}: {quantity}")
