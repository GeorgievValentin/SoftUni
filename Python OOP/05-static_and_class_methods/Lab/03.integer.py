class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if type(float_value) is not float:
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        value = value.replace("IV", "IIII").replace("IX", "VIIII")
        value = value.replace("XL", "XXXX").replace("XC", "LXXXX")
        value = value.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in value:
            number += translations[char]
        return cls(number)

    @classmethod
    def from_string(cls, value):
        if type(value) is not str:
            return "wrong type"
        try:
            return cls(int(value))
        except ValueError:
            return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_float(2.6))
print(Integer.from_string(2.6))
print(Integer.from_string("2.6"))

