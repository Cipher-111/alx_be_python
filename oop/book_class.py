class Book:
    """
    Represents a book with a title, author, and publication year.
    Demonstrates the use of Python's magic methods:
    __init__, __del__, __str__, and __repr__.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Constructor for the Book class.
        Initializes a new Book instance with the given title, author, and year.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year
        # Removed: print(f"Book '{self.title}' created.") - This line caused the extra output.

    def __del__(self):
        """
        Destructor for the Book class.
        This method is called when the object is about to be destroyed (deleted).
        It prints a message indicating which book is being deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns the informal string representation of the Book object.
        This is typically used for end-user display (e.g., by the print() function).

        Returns:
            str: A formatted string: "(title) by (author), published in (year)".
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns the official (developer-facing) string representation of the Book object.
        This string should ideally be unambiguous and allow recreation of the object.

        Returns:
            str: A string that would recreate the Book instance:
                 f"Book('{self.title}', '{self.author}', {self.year})"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"