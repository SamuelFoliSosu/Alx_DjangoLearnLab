# advanced_features_and_security/LibraryProject/bookshelf/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/new/', views.book_create, name='book_create'),
    path('books/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),

    # New URLs for ExampleForm
    path('example-form/', views.example_form_view, name='example_form'),
    path('form-success/', views.form_success_view, name='form_success'),
]