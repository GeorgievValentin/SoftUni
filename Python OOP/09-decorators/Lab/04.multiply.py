def multiply(num):
    def decorator(ref_func):
        def wrapper(number):  # number can be named any ather way
            result = ref_func(number)
            return result * num

        return wrapper

    return decorator


@multiply(5)  # num = 5
def add_ten(number):  # number = 3
    return number + 10


print(add_ten(3))
