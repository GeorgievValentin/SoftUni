from oop.oop_exams.retake_exam_22_august_2022.project import MainDish


class Salmon(MainDish):
    GRAMS = 22

    def __init__(self, name: str, price: float):
        super().__init__(name, price, Salmon.GRAMS)

