def even_odd_filter(**kwargs):
    nums = {}

    for key, value in kwargs.items():
        if key == "even":
            nums[key] = [el for el in value if el % 2 == 0]
        else:
            nums[key] = [el for el in value if not el % 2 == 0]

    return dict(sorted(nums.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
