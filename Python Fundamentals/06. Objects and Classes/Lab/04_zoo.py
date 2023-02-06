class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, animal):
        if species == "mammal":
            self.mammals.append(animal)
        elif species == "fish":
            self.fishes.append(animal)
        elif species == "bird":
            self.birds.append(animal)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f"{species.capitalize()}s in {self.name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            return f"{species.capitalize()}es in {self.name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            return f"{species.capitalize()}s in {self.name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"


zoo_name = input()
zoo = Zoo(zoo_name)
animals_count = int(input())
for i in range(animals_count):
    species, animal = input().split()
    zoo.add_animal(species, animal)

species = input()
print(zoo.get_info(species))