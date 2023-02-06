def operate(operator, *args):
# reduce !!!

    def add():
        return sum(args)

    def subtract():
        result = args[0]
        for el in args[1:]:
            result -= el
        return result

    def multiply():
        result = 1
        for el in args:
            result *= el
        return result

    def divide():
        result = args[0]
        for el in args[1:]:
            if not el == 0:
                result /= el
        return result

    if operator == "+":
        return add()
    elif operator == "-":
        return subtract()
    elif operator == "*":
        return multiply()
    elif operator == "/":
        return divide()


print(operate("/", 1, 0, 3))