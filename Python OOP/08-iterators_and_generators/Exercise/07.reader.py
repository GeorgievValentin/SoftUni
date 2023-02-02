def read_next(*args):

    for el in args:
        for x in el:
            yield x


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
