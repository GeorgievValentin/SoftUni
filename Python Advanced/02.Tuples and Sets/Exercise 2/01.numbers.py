# set1 = set(int(el)for el in input().split())
# set2 = set(int(el)for el in input().split())
# num = int(input())
# for _ in range(num):
#     command = input().split()
#     action = command[0]
#     location = command[1]
#     # nums = [(int(el)) for el in command[2:]]
#     if "Add" in command:
#         if location == "First":
#             [set1.add(int(x)) for x in command[2:]]
#         else:
#             [set2.add(int(x)) for x in command[2:]]
#     elif "Remove" in command:
#         if location == "First":
#             set1 = set1.difference([int(x) for x in command[2:]])
#         else:
#             set2 = set2.difference([int(x) for x in command[2:]])
#     elif "Check" in command:
#         if set1.issubset(set2) or set2.issubset(set1):
#             print("True")
#         else:
#             print("False")
#
# print(*sorted(set1), sep=", ")
# print(*sorted(set2), sep=", ")
#
set1 = set(int(el)for el in input().split())
set2 = set(int(el)for el in input().split())
num = int(input())
for _ in range(num):
    command = input().split()
    action = command[0]
    location = command[1]
    nums = set(int(el)for el in command[2:(len(command) + 1)])
    if "Add" in command:
        if location == "First":
            set1 = set1.union(nums)
        else:
            set2 = set2.union(nums)
    elif "Remove" in command:
        if location == "First":
            set1 = set1.difference(nums)
        else:
            set2 = set2.difference(nums)
    elif "Check" in command:
        if set1.issubset(set2) or set2.issubset(set1):
            print("True")
        else:
            print("False")
print(*sorted(set1), sep=", ")
print(*sorted(set2), sep=", ")
