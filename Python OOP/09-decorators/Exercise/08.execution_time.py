from time import time


def exec_time(func):
    def wrapper(*args):
        start = time()
        func(*args)
        end = time()

        return end - start

    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 100_000_000))


#  10 000 000 - 2.066342353820801

#  100 000 000 - 18.277104377746582
