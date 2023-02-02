from oop.oop_exams.retake_exam_22_august_2022.project import Mammal


class Bear(Mammal):
    def __init__(self, name):
        super().__init__(name)


# mammal = Mammal("Stella")
# print(mammal.__class__.__bases__[0].__name__)
# print(mammal.name)
