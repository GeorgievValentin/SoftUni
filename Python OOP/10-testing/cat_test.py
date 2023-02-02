class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


from unittest import TestCase, main


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat("Gencho")

    def test_cats_size_is_increased_after_eat(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_can_cat_eat_after_fed_raises(self):
        self.cat.eat()
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual("Already fed.", str(ex.exception))

    def test_can_cat_sleep_if_not_fed_raises(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_cat_is_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()
