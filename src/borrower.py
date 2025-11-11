class Borrower:
    def __init__(self, name, contact, membership_id):
        self.name = name
        self.contact = contact
        self.membership_id = membership_id
        self.borrowed_books = []  

    def update_contact(self, new_contact):
        """Update borrower contact details."""
        self.contact = new_contact

    def borrow_book(self, book, due_date):
        """Add a book to the borrowed list."""
        self.borrowed_books.append((book, due_date))

    def return_book(self, isbn):
        """Return a book based on ISBN."""
        for borrowed in self.borrowed_books:
            if borrowed[0].isbn == isbn:
                self.borrowed_books.remove(borrowed)
                return True
        return False

    def __str__(self):
        return f"Member: {self.name} | ID: {self.membership_id} | Contact: {self.contact}"
