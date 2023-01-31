from collections import deque


def stock_availability(inventory: list, action: str, *args):
    if action == "delivery":
        inventory.extend(args)
    else:
        if args:
            for el in args:
                if str(el).isdigit():
                    inventory = deque(inventory)
                    for i in range(int(el)):
                        inventory.popleft()
                while el in inventory:
                    inventory.remove(el)
        else:
            inventory = deque(inventory)
            inventory.popleft()
    return list(inventory)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
