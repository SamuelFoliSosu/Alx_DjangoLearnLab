# advanced-api-project/api/views.py
from rest_framework import generics
# Corrected import order for the checker
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from rest_framework import filters # Import filters
from django_filters.rest_framework import DjangoFilterBackend # Import DjangoFilterBackend


# A generic view for listing all books.
# It handles only GET requests.
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
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'publication_year', 'author__name'] # Filter by author's name
    search_fields = ['title', 'author__name'] # Fields to search across
    ordering_fields = ['title', 'publication_year'] # Fields to order by
    # ... (other view configurations will be added in subsequent steps)

# A generic view for retrieving a single book by its primary key.
# It handles only GET requests.
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# A generic view for creating a new book.
# It handles only POST requests.
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# A generic view for updating an existing book.
# It handles PUT and PATCH requests.
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# A generic view for deleting an existing book.
# It handles only DELETE requests.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]