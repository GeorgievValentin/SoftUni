months = int(input())
wather = 20
internet = 15
others = 0
total_bill = 0
total_electrivity = 0

for i in range(months):
    electricity = float(input())
    total_electrivity += electricity
    others += (electricity + wather + internet) * 1.2
totatl_wather = wather * months
total_internet = internet * months
total_bill = totatl_wather + total_internet + others + total_electrivity
average_bill = total_bill / months

print(f"Electricity: {total_electrivity:.2f} lv")
print(f"Water: {totatl_wather:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {others:.2f} lv")
print(f"Average: {average_bill:.2f} lv")
