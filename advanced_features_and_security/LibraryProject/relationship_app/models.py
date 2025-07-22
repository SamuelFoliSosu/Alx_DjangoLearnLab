# # django-models/relationship_app/models.py
# from django.db import models
# from django.contrib.auth.models import User

# class Author(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
#     # publication_date = models.DateField()
#     # isbn = models.CharField(max_length=13, unique=True)
#     # Use related_name='books' to access books from an author instance: author_instance.books.all()

#     def __str__(self):
#         return self.title

# class Library(models.Model):
#     name = models.CharField(max_length=100)
#     books = models.ManyToManyField(Book, related_name='libraries')
#     # Use related_name='libraries' to access libraries from a book instance: book_instance.libraries.all()

#     class Meta:
#         # Define custom permissions here
#         permissions = [
#             ("can_add_book", "Can add book"),
#             ("can_change_book", "Can change book"),
#             ("can_delete_book", "Can delete book"),
#         ]

#     def __str__(self):
#         return self.name

# class Librarian(models.Model):
#     name = models.CharField(max_length=100)
#     library = models.OneToOneField(Library, on_delete=models.CASCADE, primary_key=True, related_name='librarian')
#     # primary_key=True makes the Librarian's primary key also the foreign key to Library,
#     # ensuring a true 1-to-1 where each Librarian IS a specific Library's librarian.
#     # related_name='librarian' allows accessing the librarian from a library instance: library_instance.librarian

#     def __str__(self):
#         return self.name
    
# class UserProfile(models.Model):
#     # Define choices for user roles
#     ROLE_CHOICES = (
#         ('Admin', 'Admin'),
#         ('Librarian', 'Librarian'),
#         ('Member', 'Member'),
#     )

#     # One-to-one relationship with Django's User model
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Role field with predefined choices, default to 'Member'
#     role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

#     def __str__(self):
#         # String representation for the UserProfile object
#         return f"{self.user.username}'s Profile ({self.role})"
