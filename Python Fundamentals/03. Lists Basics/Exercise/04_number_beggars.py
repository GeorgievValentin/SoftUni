money_as_string = input().split(", ")
beggars = int(input())
sum_for_each_beggar = []


for beggar in range(beggars):
    current_sum = 0
    for sums in range(beggar, len(money_as_string), beggars):
        current_sum += int(money_as_string[sums])

    sum_for_each_beggar.append(current_sum)
print(sum_for_each_beggar)
