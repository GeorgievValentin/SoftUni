from oop.oop_exams.regular_exam_14_august_2022.project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        if self.speed <= 118:
            self.speed += 2
        elif self.speed < 120:
            self.speed = 120

