from itertools import permutations as perm


def possible_permutations(elements: list):
    for el in perm(elements):
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]
