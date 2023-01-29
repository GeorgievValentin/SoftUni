numbers = [int(x) for x in input().split()]
target_number = int(input())
unique_pairs = set()
iterations = 0

for i in range(0, len(numbers)):
    for j in range(i + 1, len(numbers)):
        a = numbers[i]
        b = numbers[j]
        if a + b == target_number:
            unique_pairs.add((a, b))
            print(f'{a} + {b} = {target_number}')
        iterations += 1

print(f'Iterations done: {iterations}')

for pair in unique_pairs:
    print(f"{pair[0]} + {pair[1]} = {target_number}")
