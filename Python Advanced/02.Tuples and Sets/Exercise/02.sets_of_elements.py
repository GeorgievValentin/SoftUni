n, m = input().split()
num1 = int(n)
num2 = int(m)

set1 = set()
set2 = set()

for _ in range(num1):
    set1.add(int(input()))
for _ in range(num2):
    set2.add(int(input()))

result = set1.intersection(set2)
# print({f"\num".join(result) for el in result})   ???
for el in result:
    print(el)