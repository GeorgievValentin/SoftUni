botles = int(input())
quantity_ml = botles * 750
plate_ml = 5
pot_ml = 15
plates = 0
pots = 0
counter = 0
action = input()
enough = True
while action != "End":
    counter += 1
    if counter < 3:
        quantity_ml -= int(action) * plate_ml
        plates += int(action)
    else:
        quantity_ml -= int(action) * pot_ml
        pots += int(action)
        counter = 0
    if quantity_ml < 0:
        enough = False
        break
    action = input()
if enough:
    print("Detergent was enough!")
    print(f"{plates} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {quantity_ml} ml.")
else:
    print(f"Not enough detergent, {abs(quantity_ml)} ml. more necessary!")