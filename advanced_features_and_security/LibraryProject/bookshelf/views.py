# advanced_features_and_security/LibraryProject/bookshelf/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.forms import ModelForm
# Import the Book model from where it's defined (relationship_app)
from relationship_app.models import Book, Author # Also import Author if your BookForm uses it directly

# Simple form for Book model (could be in a forms.py, but for simplicity here)
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author'] # Assuming Author is correctly set up

# View all books (anyone logged in can view)
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# View book details (requires specific permission)
# Note: The permission string is 'app_name.permission_codename'
# Since 'can_view_book' is defined on the Book model in relationship_app,
# the app_name part remains 'relationship_app'.
@permission_required('relationship_app.can_view_book', raise_exception=True)
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookshelf/book_detail.html', {'book': book})

# Create a new book (requires specific permission)
@permission_required('relationship_app.can_create_book', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form, 'action': 'Create'})

# Edit an existing book (requires specific permission)
@permission_required('relationship_app.can_edit_book', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form, 'action': 'Edit'})

# Delete a book (requires specific permission)
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})