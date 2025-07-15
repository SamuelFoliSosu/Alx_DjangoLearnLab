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