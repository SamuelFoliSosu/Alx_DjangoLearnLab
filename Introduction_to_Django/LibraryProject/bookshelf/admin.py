# bookshelf/admin.py
from django.contrib import admin
from .models import Book # Import your Book model

# Define the admin class for the Book model
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view of the admin interface
    list_display = ('title', 'author', 'publication_year')

    # Fields to use for filtering in the right sidebar of the admin list view
    list_filter = ('publication_year', 'author')

    # Fields to enable search functionality in the admin interface
    search_fields = ('title', 'author')

# Register your Book model with the custom BookAdmin class
# This tells Django to use the BookAdmin configuration when displaying
# and managing Book instances in the admin site.
admin.site.register(Book, BookAdmin)