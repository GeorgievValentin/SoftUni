from unittest import TestCase, main

from project.toy_store import ToyStore


class ToyStoreTests(TestCase):
    def setUp(self):
        self.store = ToyStore()

    def test_correct_initialization(self):
        expected = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(expected, self.store.toy_shelf)

    def test_add_toy_correctly(self):
        self.store.add_toy("A", "Car")
        result = self.store.add_toy("B", "Bear")
        expected = {
            "A": "Car",
            "B": "Bear",
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        self.assertEqual(expected, self.store.toy_shelf)
        self.assertEqual("Toy:Bear placed successfully!", result)

    def test_add_toy_in_non_existing_shelf_raises(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("H", "Car")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_existing_toy_in_shelf_raises(self):
        self.store.add_toy("A", "Car")
        self.store.add_toy("B", "Bear")
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Car")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_in_taken_shelf_raises(self):
        self.store.add_toy("A", "Car")
        self.store.add_toy("B", "Bear")
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Doll")
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_remove_toy_correctly(self):
        self.store.add_toy("A", "Car")
        self.store.add_toy("B", "Bear")
        result = self.store.remove_toy("B", "Bear")

        expected = {
            "A": "Car",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(expected, self.store.toy_shelf)
        self.assertEqual("Remove toy:Bear successfully!", result)

    def test_remove_toy_from_non_existing_shelf_raises(self):
        self.store.add_toy("A", "Car")
        self.store.add_toy("B", "Bear")
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("H", "Car")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_non_existing_toy_from_shelf_raises(self):
        self.store.add_toy("A", "Car")
        self.store.add_toy("B", "Bear")
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "Doll")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))




if __name__ == "__main__":
    main()