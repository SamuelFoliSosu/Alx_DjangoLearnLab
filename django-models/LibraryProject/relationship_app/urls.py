from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books
from .views import LibraryDetailView
from .views import add_author
from .views import add_book
from .views import register
from django.conf import settings
from . import views

app_name = 'relationship_app'

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('authors/add/', add_author, name='add_author'),
    path('books/add_book/', add_book, name='add_book'),

    # New Authentication URL patterns
    path('register/', views.register, name='register'), # Your custom registration view
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html', next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),

    # NEW: Role-based access control URLs
    path('admin-dashboard/', views.admin_view, name='admin_dashboard'),
    path('librarian-dashboard/', views.librarian_view, name='librarian_dashboard'),
    path('member-dashboard/', views.member_view, name='member_dashboard'),

    # NEW: Secured Book Action URLs
    path('books/<int:pk>/edit_book/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete_book/', views.delete_book, name='delete_book'),
]