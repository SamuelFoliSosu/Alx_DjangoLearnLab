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