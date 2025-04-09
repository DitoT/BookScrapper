class Book:
    """
    This class models a book with attributes like title, price, availability,
    and description. It provides methods to represent the book as a dictionary.
    """

    def __init__(self, title, price, availability, description):
        self.title = title
        self.price = self._validate_price(price)
        self.availability = availability
        self.description = description

    def _validate_price(self, price):
        """
        Validates that the price is a float.
        If the price is invalid or missing, it defaults to 0.0.
        """
        try:
            """""
            Strip any unwanted characters (e.g., '£', '€') and
            attempt to convert to float
            """
            price = float(
                str(price)
                .strip()
                .replace('£', '')
                .replace('€', '')
                .replace('$', '')
            )

            return price
        except (ValueError, TypeError):
            print(f"Invalid price: {price}. Defaulting to 0.0")
            return 0.0

    def to_dict(self):
        """
        Converts the Book object into a dictionary.
        """
        return {
            "title": self.title,
            "price": self.price,
            "availability": self.availability,
            "description": self.description
        }


class BookCollection:
    """
    This class models a collection of Book objects.
    It provides methods to add books and
    calculate the average price of the collection.
    """

    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Adds a book to the collection."""
        self.books.append(book)

    def get_average_price(self):
        """Calculates the average price of books in the collection."""
        if not self.books:
            return 0.0  # No books in the collection
        total_price = sum(book.price for book in self.books)
        return total_price / len(self.books)
