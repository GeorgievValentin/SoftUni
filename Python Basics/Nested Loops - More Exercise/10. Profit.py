one_lv_count = int(input())
two_lv_count = int(input())
five_lv_count = int(input())
sum_lv = int(input())

one_lv_sum = one_lv_count
two_lv_sum = two_lv_count * 2
five_lv_sum = five_lv_count * 5

for a in range(one_lv_count + 1):
    for b in range(two_lv_count + 1):
        for c in range(five_lv_count + 1):
            if a + b * 2 + c * 5 == sum_lv:
                print(f"{a} * 1 lv. + {b} * 2 lv. + {c} * 5 lv. = {sum_lv} lv.")