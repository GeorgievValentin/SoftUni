def check_is_it_palindrome(text):
    if text == text[::-1]:
        return True
    return False


nums = input().split(", ")
for num in nums:
    is_palindrome = check_is_it_palindrome(num)
    print(is_palindrome)
