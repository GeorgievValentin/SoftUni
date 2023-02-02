from oop.oop_exams.retake_exam_22_august_2022.project import Reptile


class Lizard(Reptile):
    def __init__(self, name):
        super().__init__(name)


# lizard = Lizard("John")
# print(lizard.__class__.__bases__[0].__name__)
# print(lizard.name)
