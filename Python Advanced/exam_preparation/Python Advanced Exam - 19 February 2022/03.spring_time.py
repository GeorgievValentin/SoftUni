def start_spring(**kwargs):
    current_dict = {}
    for key, value in kwargs.items():
        if value not in current_dict:
            current_dict[value] = []
        current_dict[value].append(key)
    sorted_dict = sorted(current_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""
    for el in sorted_dict:
        type_object = el[0]
        list_of_objects = el[1]
        sorted_list = sorted(list_of_objects)
        result += f"{type_object}:\n"
        for obj in sorted_list:
            result += f"-{obj}\n"
    return result


example_objects = {
    "Water Lilly": "flower",
    "Swifts": "bird",
    "Callery Pear": "tree",
    "Swallows": "bird",
    "Dahlia": "flower",
    "Tulip": "flower",
}
print(start_spring(**example_objects))

example_objects = {
    "Swallow": "bird",
    "Thrushes": "bird",
    "Woodpeckers": "bird",
    "Swallows": "bird",
    "Warblers": "bird",
    "Shrikes": "bird",
}
print(start_spring(**example_objects))

example_objects = {
    "Magnolia": "tree",
    "Swallow": "bird",
    "Thrushes": "bird",
    "Pear": "tree",
    "Cherries": "tree",
    "Shrikes": "bird",
    "Butterfly": "insect"
}
print(start_spring(**example_objects))
