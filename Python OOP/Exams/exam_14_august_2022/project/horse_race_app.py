from oop.oop_exams.regular_exam_14_august_2022.project.horse_race import HorseRace
from oop.oop_exams.regular_exam_14_august_2022.project.horse_specification.appaloosa import Appaloosa
from oop.oop_exams.regular_exam_14_august_2022.project.horse_specification.thoroughbred import Thoroughbred
from oop.oop_exams.regular_exam_14_august_2022.project.jockey import Jockey


class HorseRaceApp:
    HORSE_TYPES = ["Appaloosa", "Thoroughbred"]

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def __get_jockey(self, jockey_name: str):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:

                return jockey
        raise Exception(f"Jockey {jockey_name} could not be found!")

    def __get_horse(self, horse_type: str):
        for horse in reversed(self.horses):
            if horse.__class__.__name__ == horse_type and not horse.is_taken:

                return horse
        raise Exception(f"Horse breed {horse_type} could not be found!")

    def __get_race(self, race_type: str):
        for race in self.horse_races:
            if race.race_type == race_type:

                return race
        raise Exception(f"Race {race_type} could not be found!")

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        for horse in self.horses:
            if horse.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type not in self.HORSE_TYPES:
            return

        new_horse = None

        if horse_type == self.HORSE_TYPES[0]:
            new_horse = Appaloosa(horse_name, horse_speed)

        elif horse_type == self.HORSE_TYPES[1]:
            new_horse = Thoroughbred(horse_name, horse_speed)

        self.horses.append(new_horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        for race in self.horse_races:
            if race.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__get_jockey(jockey_name)
        horse = self.__get_horse(horse_type)
        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True

        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        jockey = self.__get_jockey(jockey_name)
        race = self.__get_race(race_type)

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.__get_race(race_type)

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = sorted(race.jockeys, key=lambda jockey: -jockey.horse.speed)[0]
        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}!" \
               f" Winner's horse: {winner.horse.name}."
