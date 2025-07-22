# advanced_features_and_security/relationship_app/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Author, Book, Library, Librarian # Import all your models

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

# Register your other models as they were before
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)