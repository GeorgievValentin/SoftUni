num = int(input())
reservations = set()
for _ in range(num):
    reservation = input()
    reservations.add(reservation)

guest = input()
while not guest == "END":
    reservations.remove(guest)
    guest = input()

print(len(reservations))
print("\n".join(sorted(reservations)))
