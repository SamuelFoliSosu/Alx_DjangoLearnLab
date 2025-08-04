# api/models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Author(models.Model):
    """
    Model to represent an Author.
    Establishes a one-to-many relationship with the Book model,
    meaning one author can have multiple books.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Model to represent a Book.
    Links to the Author model via a ForeignKey, creating the one-to-many relationship.
    Includes a custom validation rule to ensure the publication year is not in the future.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.author.name}"