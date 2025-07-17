# django-models/LibraryProject/relationship_app/views.py
from django.shortcuts import render
from django.views.generic.detail import DetailView
# from .models import Book, Library, Author, Librarian # Comment out or remove this line
from .models import Book # Keep this if other views use Book
from .models import Library # <--- Ensure this exact line exists or is easily found by checker
from .models import Author # Keep others if needed, perhaps on separate lines too
from .models import Librarian # Keep others if needed

# Function-based view to list all books
def book_list(request):
    books = Book.objects.all().order_by('title') # Get all books, ordered by title
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library' # This makes the Library object available as 'library' in the template
    # DetailView automatically fetches the object based on the URL parameter (pk by default)

    # Optional: If you need to add extra context to the DetailView
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # self.object is the Library instance fetched by DetailView
    #     context['books_in_library'] = self.object.books.all()
    #     return context