def repeat_string_n_times(text, number):
    return text * number


txt = input()
num = int(input())
result = repeat_string_n_times(txt, num)
print(result)


# lambda
repeat_string_n_times = lambda text, number: text * number

txt = input()
num = int(input())
result = repeat_string_n_times(txt, num)
print(result)
