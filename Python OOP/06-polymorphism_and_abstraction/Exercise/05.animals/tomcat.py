from oop.oop_exams.retake_exam_22_august_2022.project import Cat


class Tomcat(Cat):
    def __init__(self, name: str, age: int, gender: str = "Male"):
        super().__init__(name, age, gender)

    def make_sound(self):
        return "Hiss"

