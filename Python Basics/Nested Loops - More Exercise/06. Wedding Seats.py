last_sector = ord(input())
rows_first_sector = int(input())
places_in_row = int(input())
even_or_odd = ""
counter = 0
for sect in range(65, last_sector + 1):
    for row in range(1, rows_first_sector + 1):
        if row % 2 != 0:
            places = places_in_row
        else:
            places = places_in_row + 2
        for place in range(97, places + 97):
            counter += 1
            print(f"{chr(sect)}{row}{chr(place)}")
    rows_first_sector += 1
print(counter)