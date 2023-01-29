from collections import deque
# rotate(num=1)
# Rotate the deque num steps to the right. If num is negative, rotate to the left.
names = deque(input().split())
n_toss = int(input())

while len(names) > 1:
    names.rotate(- n_toss)
    print(f"Removed {names.pop()}")
print(f"Last is {names[0]}")
