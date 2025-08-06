# advanced-api-project/api/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters # Import DRF's built-in filters
from django_filters import rest_framework as filters_drf # Corrected import for django-filter

from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """ 
    A generic view for listing all books, now with filtering, searching, and ordering capabilities.
    - Filtering: Allows filtering by 'title', 'publication_year', and 'author__name'.
    - Searching: Allows searching across 'title' and 'author__name'.
    - Ordering: Allows ordering by 'title' and 'publication_year'.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # --- Filtering, Searching, Ordering Configuration ---
    filter_backends = [filters_drf.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'publication_year', 'author__name'] # Filter by author's name
    search_fields = ['title', 'author__name'] # Fields to search across
    ordering_fields = ['title', 'publication_year'] # Fields to order by

# Other views remain unchanged from previous steps
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]