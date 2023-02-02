from oop.oop_exams.retake_exam_22_august_2022.project import Food


class Dessert(Food):
    def __init__(self, name: str, price: float, grams: float, calories: float):
        super(). __init__(name, price, grams)
        self.__calories = calories

    @property
    def calories(self):
        return self.__calories
