from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base




server = 'DESKTOP-E0FLFBP\ADITYASQL'  # Replace with your server hostname or IP address
database = 'LibraryDB'  # Replace with your database name
username = 'sa'  # Replace with your SQL Server username
password = 'Password123'  # Replace with your SQL Server password

# Define the SQLAlchemy database connection
engine = create_engine(f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server')

# Create a session
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()


# Create the tables in the database
Base.metadata.create_all(engine)


# Close the session when done
def close_session():
    session.close()


# Define data models (classes):
class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Define the one-to-many relationship with Book model
    books = relationship('Book', back_populates='author')


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))

    # Define the back-reference to Author model
    author = relationship('Author', back_populates='books')


class Patron(Base):
    __tablename__ = 'patrons'
    id = Column(Integer, primary_key=True)
    name = Column(String)





