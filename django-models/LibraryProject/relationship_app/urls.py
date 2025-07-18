from django.urls import path
from .views import book_list
from .views import LibraryDetailView

app_name = 'relationship_app'

urlpatterns = [
    path('books/', book_list, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]