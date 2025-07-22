# Create your models here.
# bookshelf/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
# from django.conf import settings # Might be needed if other models in THIS file reference the user.
                               # In your case, it's not needed for Author, Book, Library, Librarian.
                               # It's only needed if a model like `Book` had `user = ForeignKey(settings.AUTH_USER_MODEL)`

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
    

# --- Custom User Model and Manager (New/Modified) ---

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    """
    Custom User model extending AbstractUser.
    - Uses email as the unique identifier.
    - Includes date_of_birth, profile_photo, and role fields.
    """
    # Define choices for user roles, integrated directly into CustomUser
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )

    username = None # Remove username field
    email = models.EmailField(_('email address'), unique=True)

    # Custom Fields from Task Description:
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    # Custom Field from your original UserProfile:
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

    USERNAME_FIELD = 'email'
    # 'email' is already implicitly required due to unique=True.
    # 'role' will have a default, so it's not strictly required on creation.
    REQUIRED_FIELDS = ['date_of_birth'] # Example: makes date_of_birth required for superusers if needed.

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} ({self.get_role_display()})" # Use get_role_display() for readable role

# --- Existing Models (No Changes Needed for their relationships here) ---
