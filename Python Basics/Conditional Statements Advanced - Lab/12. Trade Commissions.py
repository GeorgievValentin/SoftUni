town = input()
profit = float(input())

if town == "Sofia":
    if 0 <= profit <= 500:
        profit *= 0.05
    elif profit <= 1000:
        profit *= 0.07
    elif profit <= 10000:
        profit *= 0.08
    elif profit > 10000:
        profit *= 0.12
elif town == "Varna":
    if 0 <= profit <= 500:
        profit *= 0.045
    elif profit <= 1000:
        profit *= 0.075
    elif profit <= 10000:
        profit *= 0.1
    elif profit > 10000:
        profit *= 0.13
elif town == "Plovdiv":
    if 0 <= profit <= 500:
        profit *= 0.055
    elif profit <= 1000:
        profit *= 0.08
    elif profit <= 10000:
        profit *=0.12
    elif profit > 10000:
        profit *= 0.145
if (town != "Sofia" and town != "Varna" and town != "Plovdiv") or profit < 0:
    print("error")
else:
    print(f"{profit:.2f}")