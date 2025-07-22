# bookshelf/admin.py
from django.contrib import admin
from .models import Book # Import your Book model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser # Import CustomUser from this app's models
from .models import Author, Library, Librarian

class CustomUserAdmin(UserAdmin):
    """
    Custom Admin configuration for the CustomUser model,
    including role, date_of_birth, and profile_photo.
    """
    model = CustomUser
    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        'date_of_birth',
        'profile_photo',
        'role', # Include the new role field
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password', 'password2',
                'first_name', 'last_name', 'date_of_birth', 'profile_photo', 'role'
            )} # Include role in add form
        ),
    )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth', 'profile_photo', 'role')}), # Include role in change form
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'role', 'groups') # Add role to filters
    ordering = ('email',)

# Register your CustomUser model with the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)

# Define the admin class for the Book model
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view of the admin interface
    list_display = ('title', 'author')

    # Fields to use for filtering in the right sidebar of the admin list view
    list_filter = ('author',)

    # Fields to enable search functionality in the admin interface
    search_fields = ('title', 'author')


# Register your Book model with the custom BookAdmin class
# This tells Django to use the BookAdmin configuration when displaying
# and managing Book instances in the admin site.
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Librarian)