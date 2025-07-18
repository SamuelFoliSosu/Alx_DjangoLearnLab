# django-models/LibraryProject/LibraryProject/urls.py
from django.urls import path
from .views import book_list
from .views import LibraryDetailView

app_name = 'relationship_app'

urlpatterns = [
    path('books/', book_list, name='book_list'), # <--- Now directly reference book_list
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), # <--- Now directly reference LibraryDetailView
]