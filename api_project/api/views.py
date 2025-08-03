from rest_framework import generics, viewsets # Ensure viewsets is here
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny # If you need these
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet): # New ViewSet for CRUD
    queryset = Book.objects.all()
    serializer_class = BookSerializer