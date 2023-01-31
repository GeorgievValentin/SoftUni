from os import linesep


def words_sorting(*args):
    words = {}

    for el in args:
        if el not in words:
            words[el] = 0

    total = 0
    for key, value in words.items():
        result = 0
        for letter in key:
            result += ord(letter)
            words[key] = result
        total += result
    if not total % 2 == 0:
        sorted_words = sorted(words.items(), key=lambda x: -x[1])
    else:
        sorted_words = sorted(words.items(), key=lambda x: x[0])
    answer = ""
    for el in sorted_words:
        answer += f"{el[0]} - {el[1]}\n"
    return answer


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
