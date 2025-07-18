# django-models/LibraryProject/relationship_app/urls.py
from django.urls import path
from .views import book_list, LibraryDetailView # Import views from the current app

app_name = 'relationship_app' # Namespace for this app's URLs

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]