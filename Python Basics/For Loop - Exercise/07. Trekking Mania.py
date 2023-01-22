groups = int(input())
total_people = 0
musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0
for i in range(groups):
    people = int(input())
    total_people += people
    if people < 6:
        musala += people
    elif people < 13:
        monblan += people
    elif people < 26:
        kilimanjaro += people
    elif people < 41:
        k2 += people
    else:
        everest += people
musala_percent = musala / total_people * 100
monblan_percent = monblan / total_people * 100
kilimanjaro_percent = kilimanjaro / total_people * 100
k2_percent = k2 / total_people * 100
everest_percent = everest / total_people * 100

print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")