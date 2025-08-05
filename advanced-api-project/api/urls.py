# advanced-api-project/api/urls.py
from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    # URLs for the Book model's CRUD operations
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    # Adjusted URLs to include "books/update" and "books/delete" as literal strings
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]