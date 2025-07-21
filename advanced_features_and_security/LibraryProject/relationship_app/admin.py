# django-models/LibraryProject/relationship_app/admin.py

from django.contrib import admin
from .models import UserProfile, Library, Author, Book # Import all your models here
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'date_of_birth')
    
    # Fix the ordering error by specifying a field that exists
    ordering = ('email',)
    
    # Add custom fields to the admin display
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Profile', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Profile', {'fields': ('date_of_birth', 'profile_photo')}),
    )

# --- CRITICAL CHANGE HERE ---
# Register CustomUser (with its custom admin class) FIRST
admin.site.register(CustomUser, CustomUserAdmin)

# Then register other models that might depend on CustomUser
admin.site.register(UserProfile)
admin.site.register(Library)
admin.site.register(Author)
admin.site.register(Book)