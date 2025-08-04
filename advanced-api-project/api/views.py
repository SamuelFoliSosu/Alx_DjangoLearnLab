# api/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

class BookListCreateView(generics.ListCreateAPIView):
    """
    API view to list all books and create a new book.
    It uses generics.ListCreateAPIView to handle both GET and POST requests.
    This view demonstrates basic CRUD functionality for the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a single book instance.
    It uses generics.RetrieveUpdateDestroyAPIView to handle GET, PUT, PATCH, and DELETE requests
    for a specific book identified by its primary key.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]