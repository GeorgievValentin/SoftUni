from oop.oop_exams.retake_exam_22_august_2022.project import Dessert


class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name: str):
        super().__init__(name, Cake.PRICE, Cake.GRAMS, Cake.CALORIES)
        