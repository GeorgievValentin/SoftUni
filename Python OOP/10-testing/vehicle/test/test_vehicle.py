from unittest import TestCase, main

# from oop.lab_ex_10_testing.vehicle.project.vehicle import Vehicle
from project.vehicle import Vehicle

class TestVehicle(TestCase):
    def setUp(self):
        self.car = Vehicle(50.5, 250.5)

    def test_correct_default_fuel_consumption(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_initialization_correctly(self):
        self.assertEqual(50.5, self.car.fuel)
        self.assertEqual(self.car.capacity, self.car.fuel)
        self.assertEqual(250.5, self.car.horse_power)
        self.assertEqual(self.car.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_with_not_enough_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(50)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_correctly_with_enough_fuel(self):
        self.car.drive(10)
        self.assertEqual(38, self.car.fuel)

    def test_refuel_with_more_than_needed_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(20)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_correctly(self):
        self.car.fuel = 40
        self.car.refuel(10)
        self.assertEqual(50, self.car.fuel)

    def test_correct__str__(self):
        result = str(self.car)
        expected = "The vehicle has 250.5 horse power with " \
                   "50.5 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
