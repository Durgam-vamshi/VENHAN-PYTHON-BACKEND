from src.book import Book
from src.borrower import Borrower
from src.library import Library


def safe_int_input(prompt, allow_zero=False):
    """Safely get an integer input from user."""
    while True:
        try:
            value = int(input(prompt).strip())
            if not allow_zero and value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid number. Please enter a valid integer.")


def confirm_action(prompt):
    """Simple yes/no confirmation."""
    choice = input(f"{prompt} (y/n): ").strip().lower()
    return choice == 'y'


def main():
    library = Library()

    while True:
        print("\n======Library Management System ======")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Remove Book")
        print("4. Add Borrower")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Search Book")
        print("8. Show All Books")
        print("9. Show All Borrowers")
        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()

        # --- Add Book ---
        if choice == '1':
            title = input("Enter title: ").strip()
            author = input("Enter author: ").strip()
            isbn = input("Enter ISBN: ").strip()
            genre = input("Enter genre: ").strip()
            quantity = safe_int_input("Enter quantity: ")

            # Check for duplicates before adding
            existing = [b for b in library.books if b.isbn == isbn]
            if existing:
                print("A book with this ISBN already exists.")
            else:
                library.add_book(Book(title, author, isbn, genre, quantity))

        # --- Update Book ---
        elif choice == '2':
            isbn = input("Enter ISBN of book to update: ").strip()
            field = input("Enter field to update (title/author/genre/quantity): ").lower().strip()

            if field not in ["title", "author", "genre", "quantity"]:
                print("Invalid field name.")
                continue

            value = input("Enter new value: ").strip()
            if field == "quantity":
                try:
                    value = int(value)
                except ValueError:
                    print("Quantity must be a number.")
                    continue

            library.update_book(isbn, **{field: value})

        # --- Remove Book ---
        elif choice == '3':
            isbn = input("Enter ISBN of book to remove: ").strip()
            if confirm_action(f"Are you sure you want to remove the book (ISBN: {isbn})?"):
                library.remove_book(isbn)
            else:
                print("Book removal cancelled.")

        # --- Add Borrower ---
        elif choice == '4':
            name = input("Enter borrower name: ").strip()
            contact = input("Enter contact: ").strip()
            membership_id = input("Enter membership ID: ").strip()

            # Check for duplicates before adding
            existing = [b for b in library.borrowers if b.membership_id == membership_id]
            if existing:
                print("A borrower with this membership ID already exists.")
            else:
                library.add_borrower(Borrower(name, contact, membership_id))

        # --- Borrow Book ---
        elif choice == '5':
            membership_id = input("Enter membership ID: ").strip()
            isbn = input("Enter book ISBN: ").strip()
            library.borrow_book(membership_id, isbn)

        # --- Return Book ---
        elif choice == '6':
            membership_id = input("Enter membership ID: ").strip()
            isbn = input("Enter book ISBN: ").strip()
            library.return_book(membership_id, isbn)

        # --- Search Book ---
        elif choice == '7':
            keyword = input("Enter keyword to search: ").strip()
            results = library.search_books(keyword)
            if results:
                print("\n---Search Results ---")
                for book in results:
                    print(book)
            else:
                print("No books found matching that keyword.")

        # --- Show All Books ---
        elif choice == '8':
            print("\n--- All Books ---")
            library.show_all_books()

        # --- Show All Borrowers ---
        elif choice == '9':
            print("\n--- All Borrowers ---")
            library.show_all_borrowers()

        # --- Exit ---
        elif choice == '0':
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option (0-9).")


if __name__ == "__main__":
    main()

