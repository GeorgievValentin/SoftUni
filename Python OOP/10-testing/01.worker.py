class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker("Stamat", 100, 10)

    def test_set_all_attributes(self):
        self.assertEqual("Stamat", self.worker.name)
        self.assertEqual(100, self.worker.salary)
        self.assertEqual(10, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_worker_energy_incremented_after_rest(self):
        self.worker.rest()
        self.assertEqual(11, self.worker.energy)

    def test_worker_works_with_zero_or_negative_energy_raises(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_workers_salary_incremented_correctly_after_work(self):
        self.worker.work()
        self.assertEqual(100, self.worker.money)

    def test_workers_energy_decreased_after_work(self):
        self.worker.work()
        self.assertEqual(9, self.worker.energy)

    def test_workers_info_is_correct(self):
        self.worker.get_info()
        self.assertEqual("Stamat has saved 0 money.", self.worker.get_info())


if __name__ == "__main__":
    main()
