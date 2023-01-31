from collections import deque

materials = [int(x) for x in input().split()]
magics = deque(int(x) for x in input().split())

gemstone = 0
porcelain = 0
gold = 0
diamond = 0

while materials and magics:
    material = materials.pop()
    magic = magics.popleft()
    gift = material + magic

    if gift < 100:
        if gift % 2 == 0:
            gift = material * 2 + magic * 3
        else:
            gift *= 2

    if gift >= 500:
        gift /= 2

    if 100 <= gift <= 199:
        gemstone += 1

    elif 200 <= gift <= 299:
        porcelain += 1

    elif 300 <= gift <= 399:
        gold += 1

    elif 400 <= gift <= 499:
        diamond += 1

if (gemstone > 0 and porcelain > 0) or (gold > 0 and diamond > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magics:
    print(f"Magic left: {', '.join(str(x) for x in magics)}")

if diamond:
    print(f"Diamond Jewellery: {diamond}")
if gemstone:
    print(f"Gemstone: {gemstone}")
if gold:
    print(f"Gold: {gold}")
if porcelain:
    print(f"Porcelain Sculpture: {porcelain}")


