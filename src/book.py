class Book:
    def __init__(self, title, author, isbn, genre, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.quantity = quantity

    def update_details(self, title=None, author=None, genre=None, quantity=None):
        """Update book details selectively."""
        if title:
            self.title = title
        if author:
            self.author = author
        if genre:
            self.genre = genre
        if quantity is not None:
            if quantity >= 0:
                self.quantity = quantity
            else:
                print("Quantity cannot be negative.")

    def is_available(self):
        """Check if the book is available for borrowing."""
        return self.quantity > 0

    def __str__(self):
        return f"{self.title} by {self.author} | Genre: {self.genre} | ISBN: {self.isbn} | Available: {self.quantity}"
