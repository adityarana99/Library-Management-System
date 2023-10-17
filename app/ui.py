from app.database import session


from app.models import add_author, add_book, add_patron, get_book_by_id, get_books_by_author, get_patron_by_id, update_book_title, delete_patron


def run_library_management_system():
    while True:
        print("\n\n***** Library Management System *****")
        print("1. Add Author")
        print("2. Add Book")
        print("3. Add Patron")
        print("4. Get Book Details")
        print("5. Update Book Title")
        print("6. Delete Patron")
        print("0. Exit\n\n")

        choice = input("\n\nEnter your choice: \n")

        if choice == "1":
            name = input("\nEnter author name: ")
            author = add_author(session, name)
            print(f"Author {author.name} added with ID {author.id}")
        elif choice == "2":
            title = input("\nEnter book title: ")
            author_id = int(input("\nEnter author ID: "))
            book = add_book(session, title, author_id)
            print(f"Book '{book.title}' added with ID {book.id}")
        elif choice == "3":
            name = input("\nEnter patron name: ")
            patron = add_patron(session, name)
            print(f"Patron {patron.name} added with ID {patron.id}")
        elif choice == "4":
            book_id = int(input("\nEnter book ID: "))
            book = get_book_by_id(session, book_id)
            if book:
                print(f"Book Title: {book.title}")
                print(f"Author: {book.author.name}")
            else:
                print("Book not found.")
        elif choice == "5":
            book_id = int(input("\nEnter book ID: "))
            new_title = input("\nEnter new book title: ")
            updated_book = update_book_title(session, book_id, new_title)
            if updated_book:
                print(f"Book title updated to '{updated_book.title}'")
            else:
                print("Book not found.")
        elif choice == "6":
            patron_id = int(input("\nEnter patron ID: "))
            if delete_patron(session, patron_id):
                print("Patron deleted.")
            else:
                print("Patron not found.")
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")