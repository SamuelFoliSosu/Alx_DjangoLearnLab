# django-models/LibraryProject/relationship_app/urls.py
from django.urls import path
from .views import book_list           # <--- Add/ensure this exact line
from .views import LibraryDetailView   # <--- Keep this for the class-based view

app_name = 'relationship_app'

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]