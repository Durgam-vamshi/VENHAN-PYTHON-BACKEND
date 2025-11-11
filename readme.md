# 📚 Library Management System (Python OOP)

A **console-based Library Management System** built using **Python Object-Oriented Programming (OOP)** concepts.  
This project provides a simplified simulation of how a real-world library operates — allowing management of books, borrowers, and the borrowing/returning process — all while emphasizing clean class design, encapsulation, and modularity.

---

## 🎯 Objective

The goal of this project is to demonstrate how OOP principles can be applied to solve a real-world problem — managing a small-scale library.  
The system handles **book management, borrower management, book borrowing/returning,** and **search functionality**, using **in-memory storage** (lists) instead of a database for simplicity.

---

## ⚙️ Key Features

### 📘 **Book Management**
- Add new books with details like `title`, `author`, `ISBN`, `genre`, and `quantity`
- Update book details selectively
- Remove books (with borrowed copy validation)
- Display all books neatly in a table format

### 👤 **Borrower Management**
- Add new borrowers with `name`, `contact`, and `membership ID`
- Update borrower contact details
- Remove borrowers (restricted if books are still borrowed)
- Display all registered borrowers and their borrowed book counts

### 🔄 **Book Borrowing & Returning**
- Borrow books using borrower’s membership ID and book ISBN
- Automatically assign a **due date** (14 days from borrow date)
- Prevent borrowing unavailable or non-existent books
- Return books and update availability instantly

### 🔍 **Book Search & Availability**
- Search by `title`, `author`, `genre`, or `ISBN`
- Instantly view availability status (number of copies available)

---

## 🧱 OOP Concepts Applied

| Concept | Implementation |
|----------|----------------|
| **Encapsulation** | Each class manages its own data and methods |
| **Abstraction** | Library interface hides complexity from the user |
| **Composition** | `Library` class contains lists of `Book` and `Borrower` objects |
| **Polymorphism (Basic)** | Methods like `update_details()` and `__str__()` provide flexible behavior per object |

---

## 🧩 Project Structure

library-management-python/
├── src/
│ ├── book.py # Book class definition
│ ├── borrower.py # Borrower class definition
│ ├── library.py # Library class with management logic
├── main.py # Entry point with console menu
├── README.md # Project documentation
└── .gitignore # Ignores pycache and other temporary files


---

## 💻 Technologies Used

- **Language:** Python 3.8+
- **Libraries:** Only Python Standard Library (`datetime`, `timedelta`)
- **Paradigm:** Object-Oriented Programming
- **Storage:** In-memory lists (no external database)
- **Interface:** Console-based user input/output

---

## ▶️ How to Run the Project

### 1. **Clone the Repository**
```bash
git clone https://github.com/<your-username>/library-management-python.git
cd library-management-python

2. Run the Application
python main.py

3. Follow the Menu Prompts

You’ll see a menu like this:

====== 📚 Library Management System ======
1. Add Book
2. Update Book
3. Remove Book
4. Add Borrower
5. Borrow Book
6. Return Book
7. Search Book
8. Show All Books
9. Show All Borrowers
0. Exit


Simply enter the corresponding number to perform an operation.

🧠 Example Use Case
Adding a Book:
Enter title: The Alchemist
Enter author: Paulo Coelho
Enter ISBN: 12345
Enter genre: Fiction
Enter quantity: 5
✅ Book 'The Alchemist' added successfully!

Borrowing a Book:
Enter membership ID: M001
Enter book ISBN: 12345
📘 'The Alchemist' borrowed successfully by John Doe. Due: 26-11-2025

Returning a Book:
Enter membership ID: M001
Enter book ISBN: 12345
✅ 'The Alchemist' returned successfully by John Doe.

🧾 Example Data Flow

Books are stored as Book objects in the library’s list.

Borrowers are stored as Borrower objects with their own borrowed books list.

When a book is borrowed, the quantity decreases and due date is recorded.

When returned, the quantity increases and borrower’s record updates automatically.

🔒 Error Handling

The system gracefully handles:

Invalid menu inputs

Duplicate ISBNs or membership IDs

Borrowing unavailable books

Removing borrowers who still have borrowed books

Negative quantity entries

All such cases are handled with clear user messages.

📘 Future Enhancements

Add overdue tracking and fine calculation

Add persistent storage (SQLite or JSON file)

Introduce GUI (Tkinter or React frontend + Flask backend)

Export book/borrower data to CSV

🧑‍💻 Author

Vamshi Durgam
📞 9030913772
📧 durgamvamshi099@gmail.com

📄 License

This project is open-source and available under the MIT License.
Feel free to use, modify, and distribute with proper attribution.

⭐ Acknowledgements

Special thanks to all mentors, reviewers, and organizations that promote open-source learning projects.
This project is inspired by the need to help beginners understand real-world OOP design using Python.