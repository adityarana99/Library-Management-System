from app.database import Author, Book, Patron


# Define functions for CRUD operations here

# (Add) Operations
def add_author(session, name):
    author = Author(name=name)
    session.add(author)
    session.commit()
    return author

def add_book(session, title, author_id):
    book = Book(title=title, author_id=author_id)
    session.add(book)
    session.commit()
    return book

def add_patron(session, name):
    patron = Patron(name=name)
    session.add(patron)
    session.commit()
    return patron


# Read Operations
def get_book_by_id(session, book_id):
    return session.query(Book).filter_by(id=book_id).first()

def get_books_by_author(session, author_id):
    return session.query(Book).filter_by(author_id=author_id).all()

def get_patron_by_id(session, patron_id):
    return session.query(Patron).filter_by(id=patron_id).first()


# Update Operation
def update_book_title(session, book_id, new_title):
    book = get_book_by_id(session, book_id)
    if book:
        book.title = new_title
        session.commit()
        return book
    return None


# Delete Operation
def delete_patron(session, patron_id):
    patron = get_patron_by_id(session, patron_id)
    if patron:
        session.delete(patron)
        session.commit()
        return True
    return False