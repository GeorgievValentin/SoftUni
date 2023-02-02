from oop.oop_exams.retake_exam_22_august_2022.project import Starter


class Soup(Starter):
    def __init__(self, name: str, price: float, grams: float):
        super().__init__(name, price, grams)
        