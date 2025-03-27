import csv
import os

FILENAME = "library.csv"

# Agar file nahi hai to header create karega
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Title", "Author", "Genre", "Year"])

# Function: Nayi book add karna
def add_book():
    book_id = input("📖 Enter Book ID: ")
    title = input("📕 Enter Book Title: ")
    author = input("✍ Enter Author Name: ")
    genre = input("📂 Enter Genre: ")
    year = input("📅 Enter Year: ")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([book_id, title, author, genre, year])

    print(f"✅ Book '{title}' added successfully!")

# Function: Saari books dikhana
def view_books():
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        books = list(reader)

        if not books:
            print("❌ No books found!")
        else:
            print("\n📚 Library Books:")
            for book in books:
                print(f"📖 {book[1]} by {book[2]} ({book[3]}, {book[4]})")

# Function: Book search karna (title/author)
def search_book():
    keyword = input("🔍 Enter title/author to search: ").lower()
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        found = False

        for book in reader:
            if keyword in book[1].lower() or keyword in book[2].lower():
                print(f"📖 Found: {book[1]} by {book[2]} ({book[3]}, {book[4]})")
                found = True

        if not found:
            print("❌ No matching book found!")

# Function: Book update karna
def update_book():
    book_id = input("🔢 Enter Book ID to update: ")
    books = []

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        books = list(reader)

    updated = False
    for i, book in enumerate(books):
        if book[0] == book_id:
            print(f"📖 Updating {book[1]} by {book[2]}")
            books[i] = [
                book_id,
                input("📕 Enter New Title: ") or book[1],
                input("✍ Enter New Author: ") or book[2],
                input("📂 Enter New Genre: ") or book[3],
                input("📅 Enter New Year: ") or book[4],
            ]
            updated = True

    if updated:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(books)
        print("✅ Book updated successfully!")
    else:
        print("❌ Book not found!")

# Function: Book delete karna
def delete_book():
    book_id = input("🔢 Enter Book ID to delete: ")
    books = []

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        books = list(reader)

    books = [book for book in books if book[0] != book_id]

    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(books)

    print("✅ Book deleted successfully!")

# Menu system
while True:
    print("\n📚 Personal Library Management")
    print("1. ➕ Add Book")
    print("2. 📜 View Books")
    print("3. 🔎 Search Book")
    print("4. ✏ Update Book")
    print("5. ❌ Delete Book")
    print("6. 🚪 Exit")

    choice = input("➡ Enter your choice: ").strip()

    if choice == '1':
        add_book()
    elif choice == '2':
        view_books()
    elif choice == '3':
        search_book()
    elif choice == '4':
        update_book()
    elif choice == '5':
        delete_book()
    elif choice == '6':
        print("🚪 Exiting system...")
        break
    else:
        print("❌ Invalid choice, try again!")