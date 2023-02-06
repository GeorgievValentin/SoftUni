def grocery_store(**kwargs):
    products = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = ""
    for key, value in products:
        result += f"{key}: {value}" + '\n'
    return result


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
