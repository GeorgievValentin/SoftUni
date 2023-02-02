from oop.oop_exams.retake_exam_22_august_2022.project import Mammal
from oop.oop_exams.retake_exam_22_august_2022.project import Vegetable, Fruit, Meat


class Mouse(Mammal):

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
    
    @property
    def food_type(self):
        return [Fruit, Vegetable]

    @property
    def gained_weight(self):
        return 0.1

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @property
    def food_type(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.4

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @property
    def food_type(self):
        return [Meat, Vegetable]

    @property
    def gained_weight(self):
        return 0.3

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @property
    def food_type(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 1

    def make_sound(self):
        return "ROAR!!!"

