cells = input().split("#")
water = int(input())
effort = 0
total_fire = 0
final_cells = []
for cell in cells:
    cell = cell.split(" = ")
    type_of_fire = cell[0]
    value_of_cell = int(cell[1])
    if type_of_fire == "High" and not 80 < value_of_cell < 126:
        continue
    elif type_of_fire == "Medium" and not 50 < value_of_cell < 81:
        continue
    elif type_of_fire == "Low" and not 0 < value_of_cell < 51:
        continue
    if water < value_of_cell:
        continue

    water -= value_of_cell
    effort += value_of_cell * 0.25
    total_fire += value_of_cell
    final_cells.append(value_of_cell)
print("Cells:")
for cell in final_cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
