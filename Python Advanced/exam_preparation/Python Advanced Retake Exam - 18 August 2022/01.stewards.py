from collections import deque

seats = input().split(", ")
nums1 = deque(int(x) for x in input().split(", "))
nums2 = deque(int(x) for x in input().split(", "))
rotations = 0
taken_seats = []

while True:
    rotations += 1
    num1 = nums1.popleft()
    num2 = nums2.pop()
    letter = chr(num1 + num2)
    option1 = str(num1) + letter
    option2 = str(num2) + letter

    if option1 in seats:
        if option1 not in taken_seats:
            taken_seats.append(option1)
        else:
            continue
    elif option2 in seats:
        if option2 not in taken_seats:
            taken_seats.append(option2)
        else:
            continue
    else:
        nums1.append(num1)
        nums2.appendleft(num2)
    if len(taken_seats) == 3 or rotations == 10:
        break

print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotations}")


# from collections import deque
#
# seats = input().split(", ")
# nums1 = deque(int(x) for x in input().split(", "))
# nums2 = deque(int(x) for x in input().split(", "))
# rotations = 0
# taken_seats = []
#
# while True:
#     rotations += 1
#     num1 = nums1.popleft()
#     num2 = nums2.pop()
#     letter = chr(num1 + num2)
#     option1 = str(num1) + letter
#     option2 = str(num2) + letter
#
#     if option1 in seats:
#         taken_seats.append(option1)
#         seats.remove(option1)
#     elif option2 in seats:
#         taken_seats.append(option2)
#         seats.remove(option2)
#     else:
#         nums1.append(num1)
#         nums2.appendleft(num2)
#     if len(taken_seats) == 3 or rotations == 10:
#         break
#
# print(f"Seat matches: {', '.join(taken_seats)}")
# print(f"Rotations count: {rotations}")
