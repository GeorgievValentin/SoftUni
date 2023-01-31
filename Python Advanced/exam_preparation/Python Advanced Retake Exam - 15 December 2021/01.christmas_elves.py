from collections import deque

elves_energy = deque(int(x) for x in input().split())
materials_box = [int(x) for x in input().split()]


def create_toys(elves, materials):
    toys = 0
    energy = 0
    counter = 0

    while elves and materials:

        current_elf = elves.popleft()
        if current_elf < 5:
            continue
        current_material = materials.pop()
        counter += 1

        if counter % 3 == 0:
            current_material *= 2

        if current_elf >= current_material:
            current_elf -= current_material
            energy += current_material
            if counter % 5 == 0:
                elves.append(current_elf)
            else:
                elves.append(current_elf + 1)
                if counter % 3 == 0:
                    toys += 2
                else:
                    toys += 1
        else:
            if counter % 3 == 0:
                materials.append(current_material // 2)
            else:
                materials.append(current_material)
            elves.append(current_elf * 2)

    print(f"Toys: {toys}")
    print(f"Energy: {energy}")
    if elves:
        print(f"Elves left: {', '.join(str(x) for x in elves)}")
    if materials:
        print(f"Boxes left: {', '.join(str(x) for x in materials)}")


create_toys(elves_energy, materials_box)
