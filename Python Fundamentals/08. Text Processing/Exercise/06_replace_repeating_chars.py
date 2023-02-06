text = input()
current_el = ""
new_text = ""
for el in text:
    if not el == current_el:
        new_text += el
    current_el = el
print(new_text)

