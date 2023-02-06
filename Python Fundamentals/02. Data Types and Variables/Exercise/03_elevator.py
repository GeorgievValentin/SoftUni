people = int(input())
capacity = int(input())

courses = people // capacity
if not people % capacity == 0:
    courses += 1
