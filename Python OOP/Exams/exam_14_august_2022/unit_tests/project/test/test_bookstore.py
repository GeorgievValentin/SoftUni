from unittest import TestCase, main

from project.bookstore import Bookstore
# from oop.oop_exams.regular_exam_14_august_2022.tests.project.bookstore import Bookstore


class BookstoreTest(TestCase):
    def setUp(self):
        self.store = Bookstore(20)

    def test_correct_initialization(self):
        self.assertEqual(20, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store._Bookstore__total_sold_books)
        self.assertEqual(0, self.store.total_sold_books)

    def test_total_sold_books_property(self):
        self.assertEqual(self.store.total_sold_books, self.store._Bookstore__total_sold_books)

    def test_books_limit_setter_with_zero_limit_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.store.books_limit = 0
        self.assertEqual("Books limit of 0 is not valid", str(ex.exception))

    def test_books_limit_setter_with_negative_limit_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.store.books_limit = -1
        self.assertEqual("Books limit of -1 is not valid", str(ex.exception))

    def test__len__method(self):
        self.store.availability_in_store_by_book_titles = {"title 1": 5, "title 2": 5}
        self.store.receive_book("title", 5)
        result = len(self.store)
        self.assertEqual(15, result)

    def test_receive_books_more_than_possible_raises(self):
        self.store.availability_in_store_by_book_titles = {"title": 11}
        self.store.receive_book("title 3", 7)
        with self.assertRaises(Exception) as ex:
            self.store.receive_book("title 2", 10)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_books_with_new_title(self):
        self.store.availability_in_store_by_book_titles = {"title 1": 10}
        self.store.receive_book("title 2", 10)
        self.assertEqual(20, len(self.store))
        self.assertEqual({"title 1": 10, "title 2": 10}, self.store.availability_in_store_by_book_titles)

    def test_receive_books_with_existing_title(self):
        self.store.availability_in_store_by_book_titles = {"title 1": 10}
        self.store.receive_book("title 1", 10)
        self.assertEqual(20, len(self.store))
        self.assertEqual({"title 1": 20}, self.store.availability_in_store_by_book_titles)

    def test_take_new_quantity_available_books_by_title(self):
        self.store.availability_in_store_by_book_titles = {"title": 3}
        self.store.receive_book("title 3", 1)
        result = self.store.receive_book("title", 15)
        self.assertEqual("18 copies of title are available in the bookstore.", result)
        self.assertEqual(19, len(self.store))

    def test_sell_non_available_book_raises(self):
        self.store.availability_in_store_by_book_titles = {"title": 10}
        self.store.receive_book("title 3", 4)
        with self.assertRaises(Exception) as ex:
            self.store.sell_book("title 1", 3)
        self.assertEqual("Book title 1 doesn't exist!", str(ex.exception))

    def test_sell_available_book_without_enough_copies_raises(self):
        self.store.availability_in_store_by_book_titles = {"title": 10}
        self.store.receive_book("title 3", 4)
        with self.assertRaises(Exception) as ex:
            self.store.sell_book("title", 11)
        self.assertEqual("title has not enough copies to sell. Left: 10", str(ex.exception))

    def test_sell_books_correctly(self):
        self.store.availability_in_store_by_book_titles = {"title": 10}
        self.store.receive_book("title 3", 4)
        result = self.store.sell_book("title", 5)
        self.assertEqual(9, len(self.store))
        self.assertEqual(5, self.store.availability_in_store_by_book_titles["title"])
        self.assertEqual(5, self.store.total_sold_books)
        self.assertEqual("Sold 5 copies of title", result)

    def test__str__method(self):
        self.store.availability_in_store_by_book_titles = {"title 1": 10, "title 2": 5}
        self.store.sell_book("title 1", 5)

        expected = "Total sold books: 5\n" \
                   "Current availability: 10\n" \
                   " - title 1: 5 copies\n" \
                   " - title 2: 5 copies"

        self.assertEqual(expected, str(self.store))


if __name__ == "__main__":
    main()
