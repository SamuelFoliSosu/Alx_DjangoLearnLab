# Django Model CRUD Operations

This document details the Create, Retrieve, Update, and Delete (CRUD) operations performed on the `Book` model using the Django shell.

---

### Create a Book Instance

**Python Command:**
```python
from bookshelf.models import Book
book1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book1)

Expected Output:

1984 by George Orwell (1949)


### Retrieve a Book Instance

**Python Command:**
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(book.title)
print(book.author)
print(book.publication_year)

Expected Output:

1984
George Orwell
1949


### Update a Book Instance

This operation demonstrates how to retrieve an existing `Book` instance, modify one of its attributes, and save the changes back to the database.

**Python Command (in Django Shell):**
```python
from bookshelf.models import Book
# Retrieve the book by its current title. Using 'book' variable name for consistency.
book = Book.objects.get(title="1984")
# Update the title attribute
book.title = "Nineteen Eighty-Four"
# Save the changes to the database
book.save()
print(f"Updated Title: {book.title}")

Expected Output:

Nineteen Eighty-Four


### Delete a Book Instance

This operation demonstrates how to retrieve a `Book` instance and delete it from the database, followed by a confirmation that it no longer exists.

**Python Command (in Django Shell):**
```python
from bookshelf.models import Book
# Retrieve the book by its (potentially updated) title. Using 'book' variable name for consistency.
book = Book.objects.get(title="Nineteen Eighty-Four")
# Delete the book instance
book.delete()
# Confirm deletion by trying to retrieve all books
print(Book.objects.all())

Expected Output:

(<QuerySet []>)