from oop.oop_exams.retake_exam_22_august_2022.project import Cat


class Kitten(Cat):
    def __init__(self, name: str, age: int, gender: str = "Female"):
        super().__init__(name, age, gender)

    def make_sound(self):
        return "Meow"

