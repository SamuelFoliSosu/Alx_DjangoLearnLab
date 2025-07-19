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
from django.contrib.auth.decorators import login_required, user_passes_test # NEW IMPORTS
# from .models import UserProfile # No need to import UserProfile directly, access via request.user.userprofile

# Helper functions to check user roles
# These functions will be used with @user_passes_test
def is_admin(user):
    # Check if user is authenticated and has a UserProfile with 'Admin' role
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    # Check if user is authenticated and has a UserProfile with 'Librarian' role
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    # Check if user is authenticated and has a UserProfile with 'Member' role
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# Role-specific views with access control
@login_required(login_url='/app/login/') # Ensures user is logged in
@user_passes_test(is_admin, login_url='/app/login/') # Only allows 'Admin' users
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required(login_url='/app/login/') # Ensures user is logged in
@user_passes_test(is_librarian, login_url='/app/login/') # Only allows 'Librarian' users
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required(login_url='/app/login/') # Ensures user is logged in
@user_passes_test(is_member, login_url='/app/login/') # Only allows 'Member' users
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# ... (Your existing views: list_books, LibraryDetailView, add_author, add_book, register, user_logout)
# Make sure to keep all your previous views!

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