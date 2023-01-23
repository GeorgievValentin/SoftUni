operation = input()
total = 0
while operation != "NoMoreMoney":
    increase = float(operation)
    if increase < 0:
        print("Invalid operation!")
        break
    total += increase
    print(f"Increase: {increase:.2f}")
    operation = input()
print(f"Total: {total:.2f}")