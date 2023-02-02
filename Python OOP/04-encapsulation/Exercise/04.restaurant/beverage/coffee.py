from oop.oop_exams.retake_exam_22_august_2022.project import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.5

    def __init__(self, name: str, caffeine: float):
        super().__init__(name, Coffee.PRICE, Coffee.MILLILITERS)
        self.__caffeine = caffeine
        
    @property
    def caffeine(self):
        return self.__caffeine
