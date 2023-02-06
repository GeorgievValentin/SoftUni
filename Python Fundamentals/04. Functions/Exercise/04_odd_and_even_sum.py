def odd_end_even_sum(num):
    odd_sum = 0
    even_sum = 0

    for digit in num:
        if int(digit) % 2 == 1:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    return odd_sum, even_sum


number = input()
result = odd_end_even_sum(number)
print(f"Odd sum = {result[0]}, Even sum = {result[1]}")

