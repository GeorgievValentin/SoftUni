num = int(input())
synonyms = {}
for i in range(num):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)
for wrd, syn in synonyms.items():
    print(f"{wrd} - {', '.join(syn)}")
