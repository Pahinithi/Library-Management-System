Library Management System

Library Management System is a web application built using the Django web development framework in Python. It facilitates the management of library resources including books and student records.

## Getting Started

1. Install Django using pip:

``` 
pip install django
   ```


2. Set Up Virtual Environment:

   Create and activate a virtual environment using the following commands:
   ```bash
   virtualenv -p python3 venv
   source venv/bin/activate
   ```

3. Navigate to Project Directory:

   ```bash
   cd Library-Management-System
   ```

4. Database Setup and Server Run:

   Run the following commands to set up the database and start the server:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

## About Page

The Library Management System is designed to simplify the management of library resources. It includes features such as:

## Two Forms: 
The application contains forms for managing student and book records separately.
  
## Issue Book Form:
 There is a form to issue a book to a particular student. This form handles multiple transactions for a single student, enabling efficient management of borrowed books.

This system provides an intuitive interface for librarians to manage the library's collection and track book borrowing activities effectively. With its user-friendly design and robust functionality, the Library Management System streamlines library operations and enhances user experience.