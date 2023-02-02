from oop.oop_exams.retake_exam_22_august_2022.project.meals.meal import Meal


class Starter(Meal):
    def __init__(self, name: str, price: float, quantity: int = 60):
        super().__init__(name, price, quantity)

    def details(self):
        return f"Starter {self.name}: {self.price:.2f}lv/piece"
