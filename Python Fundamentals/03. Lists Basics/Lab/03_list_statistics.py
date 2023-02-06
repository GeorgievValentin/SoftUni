num = int(input())
positive_list = []
negative_list = []
for i in range(num):
    number = int(input())
    if number < 0:
        negative_list.append(number)
    else:
        positive_list.append(number)
print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {sum(negative_list)}")