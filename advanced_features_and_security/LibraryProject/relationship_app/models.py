# advanced_features_and_security/relationship_app/models.py

from django.db import models
# from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
# from django.conf import settings # Needed if other models were referencing User

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    class Meta:
        # Define Custom Permissions for the Book model
        permissions = [
            ("can_view_book", "Can view book details"),  # Using more specific names
            ("can_create_book", "Can create new books"),
            ("can_edit_book", "Can edit existing books"),
            ("can_delete_book", "Can delete books"),
        ]

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')

    class Meta:
        # Define custom permissions for Library model as per your original file
        permissions = [
            ("can_add_book", "Can add book to library"),    # These are likely about adding/removing books from Library M2M
            ("can_change_book", "Can change book in library"),
            ("can_delete_book", "Can delete book from library"),
        ]
        # Note: The 'can_add_book', 'can_change_book', 'can_delete_book' permissions here
        # are distinct from the Book model's permissions because they are defined on Library.
        # They imply control over the relationship, not the Book object itself.

    def __str__(self):
        return self.name
    
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, primary_key=True, related_name='librarian')

    def __str__(self):
        return self.name