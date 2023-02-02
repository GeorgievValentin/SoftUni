from oop.oop_exams.retake_exam_22_august_2022.project import Food


class Fruit(Food):
    def __init__(self, name: str, expiration_date: str):
        super().__init__(expiration_date)
        self.name = name


