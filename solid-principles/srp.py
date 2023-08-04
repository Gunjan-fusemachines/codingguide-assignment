# single-responsibility principle

# define the Book class
class Book:
    def __init__(self, title, author, isbn, genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author}"

    def borrow(self):
        if self.available:
            self.available = False
            return True
        else:
            return False

    def return_book(self):
        self.available = True
        return True


# define the LibraryCatalog class
class LibraryCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_book_details(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def get_all_books(self):
        return self.books

    def get_available_books(self):
        return [book for book in self.books if book.available]

    def get_borrowed_books(self):
        return [book for book in self.books if not book.available]


# main function to derive instances for class Book to class LibraryCatalog
def main():
    # Book instances
    book1 = Book("Title1", "Author1", "ISBN1", "A")
    book2 = Book("Title2", "Author2", "ISBN2", "B")
    book3 = Book("Title3", "Author3", "ISBN3", "C")

    # LibraryCatalog instance
    library = LibraryCatalog()

    # Add books to the library catalog
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Display all books in the library catalog
    print("All Books in the Library Catalog:")
    for book in library.get_all_books():
        print(book)

    # Borrow a book and display available and borrowed books
    print("\nBorrowing a Book:")
    isbn_to_borrow = "ISBN2"
    book_to_borrow = library.get_book_details(isbn_to_borrow)
    if book_to_borrow and book_to_borrow.borrow():
        print(f"{book_to_borrow} has been borrowed.")
    else:
        print("Book not available for borrowing.")

    print("\nAvailable Books:")
    for book in library.get_available_books():
        print(book)

    print("\nBorrowed Books:")
    for book in library.get_borrowed_books():
        print(book)

    # Return the borrowed book and display available and borrowed books
    print("\nReturning the Borrowed Book:")
    book_to_return = library.get_book_details(isbn_to_borrow)
    if book_to_return and book_to_return.return_book():
        print(f"{book_to_return} has been returned.")
    else:
        print("Book was not borrowed or is already returned.")

    print("\nAvailable Books:")
    for book in library.get_available_books():
        print(book)

    print("\nBorrowed Books:")
    for book in library.get_borrowed_books():
        print(book)

if __name__ == "__main__":
    main()
