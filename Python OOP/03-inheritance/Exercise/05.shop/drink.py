from oop.oop_exams.retake_exam_22_august_2022.project import Product


class Drink(Product):
    def __init__(self, name: str, quantity=10):
        self.name = name
        self.quantity = quantity
