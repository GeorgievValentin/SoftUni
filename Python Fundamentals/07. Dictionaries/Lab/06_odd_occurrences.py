words = [l_word.lower() for l_word in input().split()]
result = {}
for word in words:
    if word not in result:
        result[word] = 1
    else:
        result[word] += 1
for wrd, value in result.items():
    if not value % 2 == 0:
        print(f"{wrd}", end=" ")
