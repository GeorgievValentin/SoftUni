num = int(input())
word = input()
words_list = []
filtered_list = []
for i in range(num):
    text = input()
    words_list.append(text)
    if word in text:
        filtered_list.append(text)
print(words_list)
print(filtered_list)