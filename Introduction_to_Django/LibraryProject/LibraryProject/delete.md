### Delete a Book Instance

**Python Command:**
```python
from bookshelf.models import Book
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()
print(Book.objects.all()) # Should show an empty QuerySet