from django.shortcuts import render
from django.shortcuts import viewsets
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet): # New ViewSet for CRUD
    queryset = Book.objects.all()
    serializer_class = BookSerializer