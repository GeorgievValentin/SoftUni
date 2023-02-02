from oop.oop_exams.retake_exam_22_august_2022.project import Product


class Food(Product):
    def __init__(self, name: str, quantity=15):
        self.name = name
        self.quantity = quantity
