from oop.oop_exams.retake_exam_22_august_2022.project import Product


class Food(Product):
    def __init__(self, name: str, price: float, grams: float):
        super().__init__(name, price)
        self.__grams = grams

    @property
    def grams(self):
        return self.__grams
