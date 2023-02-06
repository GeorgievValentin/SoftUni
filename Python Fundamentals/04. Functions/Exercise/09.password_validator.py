def is_password_valid(text):
    is_valid = True
    digit_count = 0
    if not 6 <= len(text) <= 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")
    if not text.isalnum():
        is_valid = False
        print("Password must consist only of letters and digits")
    for el in text:
        if el.isdigit():
            digit_count += 1
    if digit_count < 2:
        is_valid = False
        print(f"Password must have at least 2 digits")
    return is_valid


password = input()
password_is_valid = is_password_valid(password)
if password_is_valid:
    print("Password is valid")
