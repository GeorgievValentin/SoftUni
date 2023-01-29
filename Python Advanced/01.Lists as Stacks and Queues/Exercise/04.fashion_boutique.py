stack_stock = [int(el) for el in input().split()]
rack_capacity = int(input())
racks = 0

while stack_stock:
    current_capacity = rack_capacity
    racks += 1
    while current_capacity >= stack_stock[-1]:
        current_capacity -= stack_stock.pop()
        if not stack_stock:
            break
print(racks)

