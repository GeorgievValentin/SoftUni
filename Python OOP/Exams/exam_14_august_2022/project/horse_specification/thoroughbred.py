from oop.oop_exams.regular_exam_14_august_2022.project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        if self.speed <= 137:
            self.speed += 3
        elif self.speed < 140:
            self.speed = 140
