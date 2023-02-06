messages = int(input())
message = ""
for i in range(messages):
    num = int(input())
    if num == 88:
        message = "Hello"
    elif num == 86:
        message = "How are you?"
    elif num > 88:
        message = "Bye."
    elif num < 88:
        message = "GREAT!"
    print(message)
