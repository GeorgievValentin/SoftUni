num = int(input())
names = {}
odd_set = set()
even_set = set()
for num in range(num):
    name = input()
    sum_chars = sum(ord(el) for el in name)
    names[name] = sum_chars
counter = 1
for person, value in names.items():
    value //= counter
    if value % 2 == 0:
        even_set.add(value)
    else:
        odd_set.add(value)
    counter += 1

if sum(odd_set) == sum(even_set):
    result = odd_set.union(even_set)
elif sum(odd_set) > sum(even_set):
    result = odd_set.difference(even_set)
else:
    result = odd_set.symmetric_difference(even_set)
result = [str(el) for el in result]
print(", ".join(result))
