from oop.oop_exams.retake_exam_22_august_2022.project import Animal
from oop.oop_exams.retake_exam_22_august_2022.project import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: int):
        if self.__budget < price:
            return "Not enough budget"

        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"

        self.workers.append(worker)

        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker.name} fired successfully"

    def pay_workers(self):
        salaries = 0
        for worker in self.workers:
            salaries += worker.salary
        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        tending = 0
        for animal in self.animals:
            tending += animal.money_for_care
        if self.__budget >= tending:
            self.__budget -= tending
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        lions = []
        [lions.append(animal) for animal in self.animals if animal.__class__.__name__ == "Lion"]
        tigers = []
        [tigers.append(animal) for animal in self.animals if animal.__class__.__name__ == "Tiger"]
        cheetahs = []
        [cheetahs.append(animal) for animal in self.animals if animal.__class__.__name__ == "Cheetah"]

        result = [
            f"You have {len(self.animals)} animals",
            f"----- {len(lions)} Lions:"
        ]
        result.extend(lions)

        result.append(f"----- {len(tigers)} Tigers:")
        result.extend(tigers)

        result.append(f"----- {len(cheetahs)} Cheetahs:")
        result.extend(cheetahs)

        return "\n".join(str(el) for el in result)

    def workers_status(self):
        caretakers = []
        [caretakers.append(worker) for worker in self.workers if worker.__class__.__name__ == "Caretaker"]
        keepers = []
        [keepers.append(worker) for worker in self.workers if worker.__class__.__name__ == "Keeper"]
        vets = []
        [vets.append(worker) for worker in self.workers if worker.__class__.__name__ == "Vet"]

        result = [
            f"You have {len(self.workers)} workers",
            f"----- {len(keepers)} Keepers:"
        ]
        result.extend(keepers)

        result.append(f"----- {len(caretakers)} Caretakers:")
        result.extend(caretakers)

        result.append(f"----- {len(vets)} Vets:")
        result.extend(vets)

        return "\n".join(str(el) for el in result)
