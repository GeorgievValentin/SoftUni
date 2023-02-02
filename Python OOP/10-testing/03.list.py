class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class IntegerListTests(TestCase):
    def test_is_initialized_correctly_with_empty_list(self):
        integer = IntegerList()
        self.assertEqual([], integer._IntegerList__data)

    def test_is_initialized_correctly_with_non_integers(self):
        integer = IntegerList(3.5, 8.9, "asd")
        self.assertEqual([], integer._IntegerList__data)

    def test_is_initialized_correctly_with_integers(self):
        integer = IntegerList(3, 5, "asd", 1.2)
        self.assertEqual([3, 5], integer._IntegerList__data)

    def test_get_data(self):
        integer = IntegerList(5)
        self.assertEqual([5], integer.get_data())

    def test_add_with_invalid_data_type_raises(self):
        integer = IntegerList(5)
        with self.assertRaises(ValueError) as ex:
            integer.add("7")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_with_valid_data_type(self):
        integer = IntegerList(5)
        integer.add(7)
        self.assertEqual([5, 7], integer._IntegerList__data)

    def test_remove_index_with_invalid_index_raises(self):
        integer = IntegerList(5)
        with self.assertRaises(IndexError) as ex:
            integer.remove_index(1)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index_with_valid_index(self):
        integer = IntegerList(5)
        integer.remove_index(0)
        self.assertEqual([], integer._IntegerList__data)

    def test_get_with_invalid_index_raises(self):
        integer = IntegerList(5)
        with self.assertRaises(IndexError) as ex:
            integer.get(1)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_with_valid_index(self):
        integer = IntegerList(5, 8)
        result = integer.get(1)
        self.assertEqual(8, result)

    def test_insert_with_invalid_index_raises(self):
        integer = IntegerList(5)
        with self.assertRaises(IndexError) as ex:
            integer.insert(2, 8)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_with_invalid_data_type_raises(self):
        integer = IntegerList(5)
        with self.assertRaises(ValueError) as ex:
            integer.insert(0, "8")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_with_valid_data_type_and_index(self):
        integer = IntegerList(5)
        integer.insert(0, 8)
        self.assertEqual([8, 5], integer._IntegerList__data)

    def test_get_biggest(self):
        integer = IntegerList(5, 8)
        result = integer.get_biggest()
        self.assertEqual(8, result)

    def test_get_index(self):
        integer = IntegerList(5, 8)
        result = integer.get_index(8)
        self.assertEqual(1, result)


if __name__ == "__main__":
    main()
