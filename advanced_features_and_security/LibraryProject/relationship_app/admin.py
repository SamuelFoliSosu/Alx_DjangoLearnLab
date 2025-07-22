# advanced_features_and_security/relationship_app/admin.py
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import Author, Book, Library, Librarian # Import all your models


# Register your other models as they were before
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)