symbols = int(input())
total = 0

for char in range(symbols):
    symbol = input()
    total += ord(symbol)
print(f"The sum equals: {total}")
