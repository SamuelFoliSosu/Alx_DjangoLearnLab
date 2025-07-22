# django-models/LibraryProject/relationship_app/views.py
# from django.shortcuts import render
# from django.shortcuts import get_object_or_404
# from django.views.generic.detail import DetailView
# from .models import Book
# from .models import Library
# # from .models import Author
# # from .models import Librarian
# # from .models import User
# from django.shortcuts import redirect # Ensure redirect is imported
# from django.urls import reverse # For redirecting to URL names
# from django.contrib.auth.forms import UserCreationForm # For user registration
# from django.contrib.auth import login # To log the user in after registration
# from django.contrib.auth.decorators import login_required, user_passes_test
# from django.contrib.auth.decorators import permission_required
# from .forms import BookForm, AuthorForm # NEW: Import BookForm and AuthorForm
# # from .models import UserProfile # No need to import UserProfile directly, access via request.user.userprofile

# # Helper functions to check user roles
# # These functions will be used with @user_passes_test
# def is_admin(user):
#     # Check if user is authenticated and has a UserProfile with 'Admin' role
#     return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# def is_librarian(user):
#     # Check if user is authenticated and has a UserProfile with 'Librarian' role
#     return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

# def is_member(user):
#     # Check if user is authenticated and has a UserProfile with 'Member' role
#     return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# # Role-specific views with access control
# @login_required(login_url='/app/login/') # Ensures user is logged in
# @user_passes_test(is_admin, login_url='/app/login/') # Only allows 'Admin' users
# def admin_view(request):
#     return render(request, 'relationship_app/admin_view.html')

# @login_required(login_url='/app/login/') # Ensures user is logged in
# @user_passes_test(is_librarian, login_url='/app/login/') # Only allows 'Librarian' users
# def librarian_view(request):
#     return render(request, 'relationship_app/librarian_view.html')

# @login_required(login_url='/app/login/') # Ensures user is logged in
# @user_passes_test(is_member, login_url='/app/login/') # Only allows 'Member' users
# def member_view(request):
#     return render(request, 'relationship_app/member_view.html')

# # ... (Your existing views: list_books, LibraryDetailView, add_author, add_book, register, user_logout)
# # Make sure to keep all your previous views!

# # Your existing add_author view (ensure it uses AuthorForm if needed)
# @login_required(login_url='/app/login/') # You might want to add permission here too later, e.g., can_add_author
# def add_author(request):
#     if request.method == 'POST':
#         form = AuthorForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('relationship_app:list_books') # Redirect to book list or authors list
#     else:
#         form = AuthorForm()
#     return render(request, 'relationship_app/add_author.html', {'form': form})

# # Update add_book with permission_required
# @permission_required('relationship_app.can_add_book', login_url='/app/login/')
# def add_book(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('relationship_app:list_books')
#     else:
#         form = BookForm()
#     return render(request, 'relationship_app/add_book.html', {'form': form})


# # NEW: edit_book view
# @permission_required('relationship_app.can_change_book', login_url='/app/login/')
# def edit_book(request, pk):
#     book = get_object_or_404(Book, pk=pk) # Get the book object or raise 404
#     if request.method == 'POST':
#         form = BookForm(request.POST, instance=book) # Pass instance to update existing book
#         if form.is_valid():
#             form.save()
#             return redirect('relationship_app:list_books')
#     else:
#         form = BookForm(instance=book) # Pre-populate form with existing book data
#     return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

# # NEW: delete_book view
# @permission_required('relationship_app.can_delete_book', login_url='/app/login/')
# def delete_book(request, pk):
#     book = get_object_or_404(Book, pk=pk) # Get the book object or raise 404
#     if request.method == 'POST':
#         book.delete() # Delete the book
#         return redirect('relationship_app:list_books')
#     # For GET request, display a confirmation page
#     return render(request, 'relationship_app/confirm_delete_book.html', {'book': book})


# def list_books(request):
#     books = Book.objects.all().order_by('title') # Get all books, ordered by title
#     context = {
#         'books': books
#     }
#     return render(request, 'relationship_app/list_books.html', context)

# class LibraryDetailView(DetailView):
#     model = Library
#     template_name = 'relationship_app/library_detail.html'
#     context_object_name = 'library'



# # View for user registration
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user) # Log the user in immediately after registration
#             return redirect(reverse('relationship_app:book_list')) # Redirect to a dashboard or book list
#     else:
#         form = UserCreationForm()
#     return render(request, 'relationship_app/register.html', {'form': form})