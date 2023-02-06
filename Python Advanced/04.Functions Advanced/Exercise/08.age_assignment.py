def age_assignment(*args, **kwargs):
    data = {}
    result = ""
    for key, value in kwargs.items():
        for el in args:
            if key in el:
                data[el] = value
    sorted_dict = sorted(data.items())
    for key, value in sorted_dict:
        result += f"{key} is {value} years old." + '\n'
    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
