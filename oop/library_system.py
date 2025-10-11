class Book:
    """
    Base class representing a generic book.
    Attributes: title (str), author (str).
    """
    def __init__(self, title: str, author: str):
        """
        Initializes a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a user-friendly string representation of the Book.
        """
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """
    Derived class representing an electronic book, inheriting from Book.
    Additional attribute: file_size (int).
    """
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initializes an EBook instance.

        Args:
            title (str): The title of the e-book.
            author (str): The author of the e-book.
            file_size (int): The file size of the e-book in KB.
        """
        super().__init__(title, author) # Call the base class (Book) constructor
        self.file_size = file_size

    def __str__(self):
        """
        Returns a user-friendly string representation of the EBook,
        including file size.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    Derived class representing a print book, inheriting from Book.
    Additional attribute: page_count (int).
    """
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initializes a PrintBook instance.

        Args:
            title (str): The title of the print book.
            author (str): The author of the print book.
            page_count (int): The number of pages in the print book.
        """
        super().__init__(title, author) # Call the base class (Book) constructor
        self.page_count = page_count

    def __str__(self):
        """
        Returns a user-friendly string representation of the PrintBook,
        including page count.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """
    Class demonstrating composition, managing a collection of books.
    Attributes: books (list) - stores instances of Book, EBook, and PrintBook.
    """
    def __init__(self):
        """
        Initializes a Library instance with an empty list of books.
        """
        self.books = []

    def add_book(self, book: Book):
        """
        Adds a Book, EBook, or PrintBook instance to the library's collection.

        Args:
            book (Book): An instance of Book or its derived classes.
        """
        self.books.append(book)
        # Removed: print(f"Added '{book.title}' to the library.")

    def list_books(self):
        """
        Prints the details of each book currently in the library.
        It leverages the __str__ method of each book object.
        """
        # Removed: print("\n--- Books in the Library ---")
        # Removed: if not self.books:
        # Removed:     print("The library is currently empty.")
        for book in self.books:
            print(book) # This will automatically call the appropriate __str__ method
        # Removed: print("----------------------------")