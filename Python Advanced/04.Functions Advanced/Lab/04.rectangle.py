def rectangle(length, width):
    def perimeter():
        perimeter = (length + width) * 2
        return f"Rectangle perimeter: {perimeter}"

    def area():
        area = length * width
        return f"Rectangle area: {area}"

    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"
    return area() + "\n" + perimeter()


print(rectangle('2', 10))