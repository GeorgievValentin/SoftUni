num = int(input())
elements = set()
for _ in range(num):
    current_el = input().split()
    for el in current_el:  # elements = elements.union(current_el)
        elements.add(el)

print("\n".join(elements))
