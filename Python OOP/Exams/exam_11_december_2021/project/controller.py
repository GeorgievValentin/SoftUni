# from oop.oop_exams.exam_11_december_2021.project.car.muscle_car import MuscleCar
# from oop.oop_exams.exam_11_december_2021.project.car.sports_car import SportsCar
# from oop.oop_exams.exam_11_december_2021.project.driver import Driver
# from oop.oop_exams.exam_11_december_2021.project.race import Race
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    valid_car_types = ["MuscleCar", "SportsCar"]

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def __get_car_by_type(self, car_type: str):
        reversed_cars = reversed(self.cars)
        for car in reversed_cars:
            if car.__class__.__name__ == car_type and not car.is_taken:
                return car
        else:
            raise Exception(f"Car {car_type} could not be found!")

    def __get_driver_by_name(self, name: str):
        for driver in self.drivers:
            if driver.name == name:
                return driver
        else:
            raise Exception(f"Driver {name} could not be found!")

    def __get_race_by_name(self, name: str):
        for race in self.races:
            if race.name == name:
                return race
        else:
            raise Exception(f"Race {name} could not be found!")

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.valid_car_types:
            return

        if model in [car.model for car in self.cars]:
            raise Exception(f"Car {model} is already created!")

        if car_type == "MuscleCar":
            new_car = MuscleCar(model, speed_limit)

        elif car_type == "SportsCar":
            new_car = SportsCar(model, speed_limit)

        self.cars.append(new_car)

        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if driver_name in [driver.name for driver in self.drivers]:
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)

        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if race_name in [race.name for race in self.races]:
            raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)

        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__get_driver_by_name(driver_name)
        car = self.__get_car_by_type(car_type)

        if driver.car is not None:
            old_car = driver.car
            driver.car = car
            old_car.is_taken = False
            car.is_taken = True

            return f"Driver {driver_name} changed his car from {old_car.model} to {car.model}."

        driver.car = car
        car.is_taken = True

        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__get_race_by_name(race_name)
        driver = self.__get_driver_by_name(driver_name)

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__get_race_by_name(race_name)

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        winners = sorted(race.drivers, key=lambda x: -x.car.speed_limit)[:3]
        result = []
        for driver in winners:
            driver.number_of_wins += 1
            result.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")

        return "\n".join(el for el in result)
