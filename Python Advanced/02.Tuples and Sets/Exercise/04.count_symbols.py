text = input()
result = {}
for char in text:
    if char not in result:
        result[char] = text.count(char)

for el in sorted(result.items()):
    print(f"{el[0]}: {el[1]} time/s")

