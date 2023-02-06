wanted_strings = input().split(", ")
words = input().split(", ")

result = [string for string in wanted_strings for word in words if string in word]
print(sorted(set(result), key=wanted_strings.index))

# result = []
# for string in wanted_strings:
#     for word in words:
#         if string in word:
#             result.append(string)
