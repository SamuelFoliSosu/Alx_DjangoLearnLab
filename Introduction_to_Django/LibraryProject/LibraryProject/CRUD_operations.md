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

**Python Command:**
```python
from bookshelf.models import Book
book_to_update = Book.objects.get(title="1984") # Make sure to retrieve by the original title
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()
print(book_to_update.title)

Expected Output:

Nineteen Eighty-Four


### Delete a Book Instance

**Python Command:**
```python
from bookshelf.models import Book
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()
print(Book.objects.all()) # Should show an empty QuerySet

Expected Output:

(<QuerySet []>)