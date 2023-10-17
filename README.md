# Library-Management-System

Description:
This project is a simple Library Management System implemented in Python. It demonstrates the principles of data modeling and interaction with a Microsoft SQL Server database. The system allows users to manage information about authors, books, and library patrons through a user-friendly command-line interface.

Project Structure:
The project is organized into the following components:

1. `app/` Directory:
   - Contains the core application code.
   - `database.py`: Handles database connections, defines SQLAlchemy models, and provides functions for database operations.
   - `models.py`: Defines SQLAlchemy data models for authors, books, and patrons.
   - `ui.py`: Implements the user interface for the command-line application.

2. `main.py`:
   - Serves as the entry point of the application.
   - Initializes and runs the Library Management System.

Key Features:
- Data modeling with SQLAlchemy: Demonstrates how to define data models in Python and interact with a relational database.
- CRUD Operations: Supports Create, Read, Update, and Delete operations for managing authors, books, and patrons.
- Error Handling: Implements robust error handling to provide informative feedback to users.

Usage:
1. Users can run the `main.py` script to start the Library Management System.
2. The command-line interface allows users to add authors, books, and patrons, retrieve book details, update book titles, and delete patrons.


Project Benefits:
- Illustrates the principles of data modeling in Python using SQLAlchemy.
- Demonstrates good coding practices, code organization, and error handling techniques.
- Provides a practical example of working with databases in Python.

Future Enhancements:
- The project can be extended with additional features such as book borrowing and returning.
- A web-based user interface can be developed to make it accessible via a web browser.
- Enhanced error handling and validation can be implemented for improved user experience.
