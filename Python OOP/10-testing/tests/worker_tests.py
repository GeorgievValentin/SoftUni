from unittest import TestCase, main

from oop.lab_ex_10_testing.worker import Worker


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker("Stamat", 100, 10)

    def test_set_all_attributes(self):
        self.assertEqual("Stamat", self.worker.name)
        self.assertEqual(100, self.worker.salary)
        self.assertEqual(10, self.worker.energy)
        self.assertEqual(0, self.worker.money)


if __name__ == "__main__":
    main()
