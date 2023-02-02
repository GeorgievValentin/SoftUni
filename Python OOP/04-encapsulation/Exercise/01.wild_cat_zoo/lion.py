from oop.oop_exams.retake_exam_22_august_2022.project import Animal


class Lion(Animal):
    MONEY_FOR_CARE = 50

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, Lion.MONEY_FOR_CARE)
