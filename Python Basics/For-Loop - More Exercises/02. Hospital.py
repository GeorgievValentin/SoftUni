days = int(input())
doctors = 7
treated_patients = 0
untreated_patients = 0

for i in range(1, days + 1):
    if i % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1
    curent_patients = int(input())
    if curent_patients <= doctors:
        treated_patients += curent_patients
    else:
        treated_patients += doctors
        untreated_patients += curent_patients - doctors

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")