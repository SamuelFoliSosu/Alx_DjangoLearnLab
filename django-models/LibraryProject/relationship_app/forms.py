# django-models/LibraryProject/relationship_app/forms.py

from django import forms
from .models import Book, Author # Make sure your Book and Author models are imported

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # Include all fields you want to be editable in the form
        fields = ['title', 'author']

class AuthorForm(forms.ModelForm): # Assuming you have an Author model and need a form for it
    class Meta:
        model = Author
        fields = ['name'] # Adjust fields based on your Author model