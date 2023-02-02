from oop.lab_ex_10_testing.car_manager import Car

from unittest import TestCase, main


class CarTest(TestCase):
    def setUp(self):
        self.car = Car("Subaru", "Forester", 15, 60)

    def test_correct_initialization(self):
        self.assertEqual("Subaru", self.car.make)
        self.assertEqual("Forester", self.car.model)
        self.assertEqual(15, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_with_empty_value_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_with_empty_value_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_with_negative_value_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_with_zero_value_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_negative_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_zero_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_with_negative_value_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_negative_value_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_zero_value_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_correctly(self):
        self.car.fuel_amount = 10
        self.car.refuel(10)
        self.assertEqual(20, self.car.fuel_amount)

    def test_drive_without_enough_fuel_raises(self):
        self.car.fuel_amount = 10
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_with_enough_fuel(self):
        self.car.fuel_amount = 50
        self.car.drive(100)
        self.assertEqual(35, self.car.fuel_amount)


if __name__ == "__main__":
    main()
