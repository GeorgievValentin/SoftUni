def find_number_perfect(num):
    divisors = []
    for number in range(1, num):
        if num % number == 0:
            divisors.append(number)
    if sum(divisors) == num:
        return True


n = int(input())
is_perfect = find_number_perfect(n)
if is_perfect:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
