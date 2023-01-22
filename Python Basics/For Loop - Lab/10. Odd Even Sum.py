nums = int(input())
evens = 0
odds = 0

for i in range(1, nums + 1):
    if i % 2 == 0:
        evens += int(input())
    else:
        odds += int(input())
diff = abs(evens - odds)
if evens == odds:
    print("Yes")
    print(f"Sum = {evens}")
else:
    print("No")
    print(f"Diff = {diff}")