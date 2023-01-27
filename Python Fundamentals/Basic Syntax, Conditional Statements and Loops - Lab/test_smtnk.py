sentence = "Have free hours and love children?"


def create_bigram(sentence):
    words = sentence.lower().split()
    return [(word_1, word_2) for word_1, word_2 in zip(words, words[1:])]


print(create_bigram(sentence))
