from oop.oop_exams.retake_exam_22_august_2022.project import Bird
from oop.oop_exams.retake_exam_22_august_2022.project import Vegetable, Fruit, Seed, Meat


class Owl(Bird):

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @property
    def food_type(self):
        return [Meat]
    
    @property
    def gained_weight(self):
        return 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)
    
    @property
    def food_type(self):
        return [Vegetable, Fruit, Seed, Meat]

    @property
    def gained_weight(self):
        return 0.35

    def make_sound(self):
        return "Cluck"
