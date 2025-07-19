# django-models/LibraryProject/relationship_app/views.py
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from .models import Author
from .models import Librarian

def list_books(request):
    books = Book.objects.all().order_by('title') # Get all books, ordered by title
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'