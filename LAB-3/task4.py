class Library:
    def __init__(self):
        self.books = []
    def add_book(self, title, author, status):
        self.books.append([title, author, status])

    def search_book(self, title):
        for book in self.books:
            if book[0] == title:
                return book
        return None
    def display_books(self):
        for book in self.books:
            print(book)
library = Library()
library.add_book("Book1", "Author1", "Available")
library.add_book("Book2", "Author2", "Issued")
library.display_books()

        