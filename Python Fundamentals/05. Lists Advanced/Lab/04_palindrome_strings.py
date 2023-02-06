words = input().split()
wanted_palindrome = input()
palindromes = [word for word in words if word == word[::-1]]
print(palindromes)
print(f"Found palindrome {palindromes.count(wanted_palindrome)} times")

