from datetime import datetime, timedelta


class Library:
    def __init__(self):
        self.books = []        # list of Book objects
        self.borrowers = []    # list of Borrower objects

    # ---------- BOOK MANAGEMENT ----------

    def add_book(self, book):
        self.books.append(book)
        print(f"✅ Book '{book.title}' added successfully!")

    def update_book(self, isbn, **kwargs):
        for book in self.books:
            if book.isbn == isbn:
                book.update_details(**kwargs)
                print(f"✅ Book '{book.title}' updated successfully!")
                return
        print("❌ Book not found.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                # Optional: check if borrowed
                borrowed_count = sum(
                    1 for borrower in self.borrowers if isbn in borrower.borrowed_books
                )
                if borrowed_count > 0:
                    print(f"⚠️ Cannot remove '{book.title}' — {borrowed_count} copies currently borrowed.")
                    return
                self.books.remove(book)
                print(f"🗑️ Book '{book.title}' removed successfully.")
                return
        print("❌ Book not found.")

    def search_books(self, keyword):
        results = []
        keyword_lower = keyword.lower()
        for book in self.books:
            if (keyword_lower in book.title.lower() or
                keyword_lower in book.author.lower() or
                keyword_lower in book.genre.lower() or
                keyword_lower in book.isbn.lower()):
                results.append(book)
        return results

    def show_all_books(self):
        if not self.books:
            print("❌ No books available in the library.")
            return

        print(f"{'Title':<25} {'Author':<20} {'Genre':<15} {'ISBN':<15} {'Quantity':<10}")
        print("-" * 90)
        for book in self.books:
            print(f"{book.title:<25} {book.author:<20} {book.genre:<15} {book.isbn:<15} {book.quantity:<10}")

    # ---------- BORROWER MANAGEMENT ----------

    def add_borrower(self, borrower):
        self.borrowers.append(borrower)
        print(f"✅ Borrower '{borrower.name}' added successfully!")

    def remove_borrower(self, membership_id):
        for borrower in self.borrowers:
            if borrower.membership_id == membership_id:
                if borrower.borrowed_books:
                    print(f"⚠️ Cannot remove '{borrower.name}' — books are still borrowed.")
                    return
                self.borrowers.remove(borrower)
                print(f"🗑️ Borrower '{borrower.name}' removed successfully.")
                return
        print("❌ Borrower not found.")

    def show_all_borrowers(self):
        if not self.borrowers:
            print("❌ No borrowers registered.")
            return

        print(f"{'Name':<25} {'Contact':<20} {'Membership ID':<20} {'Borrowed Books':<15}")
        print("-" * 90)
        for borrower in self.borrowers:
            borrowed_count = len(borrower.borrowed_books)
            print(f"{borrower.name:<25} {borrower.contact:<20} {borrower.membership_id:<20} {borrowed_count:<15}")

    # ---------- BORROW / RETURN ----------

    def borrow_book(self, membership_id, isbn):
        borrower = next((b for b in self.borrowers if b.membership_id == membership_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)

        if not borrower:
            print("❌ Borrower not found.")
            return
        if not book:
            print("❌ Book not found.")
            return
        if book.quantity <= 0:
            print("⚠️ No copies available for borrowing.")
            return

        book.quantity -= 1
        due_date = datetime.now() + timedelta(days=14)
        borrower.borrow_book(isbn, due_date)
        print(f"📘 '{book.title}' borrowed successfully by {borrower.name}. Due: {due_date.strftime('%d-%m-%Y')}")

    def return_book(self, membership_id, isbn):
        borrower = next((b for b in self.borrowers if b.membership_id == membership_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)

        if not borrower:
            print("❌ Borrower not found.")
            return
        if not book:
            print("❌ Book not found.")
            return

        if isbn not in borrower.borrowed_books:
            print("⚠️ This borrower did not borrow that book.")
            return

        borrower.return_book(isbn)
        book.quantity += 1
        print(f"✅ '{book.title}' returned successfully by {borrower.name}.")
