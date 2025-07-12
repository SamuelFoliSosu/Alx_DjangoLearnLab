### Update a Book Instance

**Python Command:**
```python
from bookshelf.models import Book
book_to_update = Book.objects.get(title="1984") # Make sure to retrieve by the original title
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()
print(book_to_update.title)