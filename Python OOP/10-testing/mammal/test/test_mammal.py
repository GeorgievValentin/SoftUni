# from oop.lab_ex_10_testing.mammal.project.mammal import Mammal
from project.mammal import Mammal
from unittest import TestCase, main


class MammalTests(TestCase):
    def setUp(self):
        self.mammal = Mammal("Stamat", "cat", "meow")

    def test_initialization_correctly(self):
        self.assertEqual("Stamat", self.mammal.name)
        self.assertEqual("cat", self.mammal.type)
        self.assertEqual("meow", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual("Stamat makes meow", result)

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_info(self):
        result = self.mammal.info()
        self.assertEqual("Stamat is of type cat", result)


if __name__ == "__main__":
    main()
