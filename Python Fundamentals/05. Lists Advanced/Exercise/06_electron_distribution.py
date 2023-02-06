electrons = int(input())
number = 1

filled_shells = []
while electrons > 0:
    max_num_in_electron = 2 * number ** 2
    if max_num_in_electron <= electrons:
        filled_shells.append(max_num_in_electron)
    else:
        filled_shells.append(electrons)
    electrons -= max_num_in_electron
    number += 1
print(filled_shells)
