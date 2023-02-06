num = int(input())
even = []
odd = []
positive = []
negative = []

for i in range(num):
    number = int(input())
    if number % 2 == 0:
        even.append(number)
    if number % 2 == 1:
        odd.append(number)
    if number < 0:
        negative.append(number)
    else:
        positive.append(number)
command = input()
if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "negative":
    print(negative)
else:
    print(positive)