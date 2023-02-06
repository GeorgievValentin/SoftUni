def sorting_cheeses(**kwargs):
    result = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result_string = ""
    for cheese, peaces in result:
        sorted_values = sorted(peaces, reverse=True)
        result_string += cheese + "\n"
        result_string += "\n".join(str(x) for x in sorted_values) + "\n"
    return result_string


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
