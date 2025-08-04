# api/serializers.py
from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
    """
    A serializer for the Book model.
    It includes a custom validation method to ensure the publication_year
    is not in the future, providing data integrity.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Custom validator for the publication_year field.
        Raises a ValidationError if the publication year is in the future.
        """
        if value > timezone.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    A serializer for the Author model.
    It includes a nested BookSerializer to handle the related books,
    demonstrating how to manage one-to-many relationships in a serialized output.
    The 'books' field is read-only to prevent books from being created or updated
    via the Author serializer.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']