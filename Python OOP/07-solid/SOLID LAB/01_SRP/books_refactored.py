class Book:
    def __init__(self, title, author, pages: int):
        self.title = title
        self.author = author
        self.pages = pages
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __repr__(self):
        return f"{self.title}: {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def find_book(self, title: str):
        try:
            book = [b for b in self.books if b.title == title][0]
            return book
        except IndexError:
            return "Book not found"

    def add_book(self, book: Book):
        self.books.append(book)

        return f"\"{book.title}\" writen by {book.author} added successfully"

    def remove_book(self, title: str):
        try:
            book = [b for b in self.books if b.title == title][0]
            self.books.remove(book)

            return f"\"{book.title}\" writen by {book.author} removed successfully"

        except IndexError:
            return "Book not found"


book_1 = Book("Code with Finesse", "Ines Kenova", 53)
book_2 = Book("Test 1", "Test 2", 69)
library = Library()
print(library.add_book(book_1))
print(library.add_book(book_2))
print(library.remove_book("test 3"))
print(library.remove_book("Test 1"))
print(library.books)
