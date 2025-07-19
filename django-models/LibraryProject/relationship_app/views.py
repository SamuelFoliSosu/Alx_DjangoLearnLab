# django-models/LibraryProject/relationship_app/views.py
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
# from .models import Author
# from .models import Librarian
from django.shortcuts import redirect # Ensure redirect is imported
from django.urls import reverse # For redirecting to URL names
from django.contrib.auth.forms import UserCreationForm # For user registration
from django.contrib.auth import login # To log the user in after registration


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

# View for user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Log the user in immediately after registration
            return redirect(reverse('relationship_app:book_list')) # Redirect to a dashboard or book list
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})