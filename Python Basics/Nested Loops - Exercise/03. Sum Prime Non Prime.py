prime_numbers = 0
non_prime_numbers = 0
number = input()
while number != "stop":
    num = int(number)
    if num < 0:
        print("Number is negative.")
    else:
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        if prime:
            prime_numbers += num
        else:
            non_prime_numbers += num
    number = input()
print(f"Sum of all prime numbers is: {prime_numbers}")
print(f"Sum of all non prime numbers is: {non_prime_numbers}")