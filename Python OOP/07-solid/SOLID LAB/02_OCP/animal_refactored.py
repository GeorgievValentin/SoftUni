from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return "meow meow"


class Dog(Animal):
    def make_sound(self):
        return "woof woof"


class Chicken(Animal):
    def make_sound(self):
        return "pew pew"


class Snake(Animal):
    def make_sound(self):
        return "ssSSss"


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Chicken(), Snake()]
animal_sound(animals)
