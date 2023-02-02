from oop.oop_exams.retake_exam_22_august_2022.project import Beverage


class ColdBeverage(Beverage):
    def __init__(self, name: str, price: float, milliliters: float):
        super().__init__(name, price, milliliters)
