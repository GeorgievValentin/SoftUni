def palindrome(word: str, index: int):
    if index == len(word) // 2:
        return f"{word} is a palindrome"

    first_letter, last_letter = word[index], word[-1 - index]
    if not first_letter == last_letter:
        return f"{word} is not a palindrome"

    return palindrome(word, index + 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))