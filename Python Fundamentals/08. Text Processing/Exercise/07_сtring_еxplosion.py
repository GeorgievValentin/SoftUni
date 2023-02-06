text = input()
for el in text:
    if el == ">":
        if text[text.index(">") + 1].isnumeric():
            number = text[text.index(">") + 1]
            if int(number) == 1:
                text = text.replace(number, "")



        # for num in range(text.index(">") + 1, text.index(">") + 1 )
print(text)
# second_start_index =
# print(int(text[text.index(">") + 1]))
# for el in text:
#     if el == ">":
#
#         if text[text.index(">") + 1] == 1:
#             text = text.replace(text[text.index(">") + 1], "")
# print(text)
#

