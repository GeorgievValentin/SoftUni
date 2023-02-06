nums = [int(num) for num in input().split(", ")]
positive = [str(num) for num in nums if num >= 0]
negative = [str(num) for num in nums if num < 0]
even = [str(num) for num in nums if num % 2 == 0]
odd = [str(num) for num in nums if not num % 2 == 0]
print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")
