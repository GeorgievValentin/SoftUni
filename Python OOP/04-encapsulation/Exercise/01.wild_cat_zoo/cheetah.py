from oop.oop_exams.retake_exam_22_august_2022.project import Animal


class Cheetah(Animal):
    MONEY_FOR_CARE = 60

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, Cheetah.MONEY_FOR_CARE)


