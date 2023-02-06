def even_numbers(number):
    even_nums = []
    for digit in number:
        digit_as_int = int(digit)
        if digit_as_int % 2 == 0:
            even_nums.append(digit_as_int)
    return even_nums


nums = input().split()
result = even_numbers(nums)
print(result)


