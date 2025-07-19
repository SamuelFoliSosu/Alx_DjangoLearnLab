from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books
from .views import LibraryDetailView
# from .views import add_author
# from .views import add_book
from .views import register

app_name = 'relationship_app'

urlpatterns = [
    path('books/', list_books, name='book_list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    # path('authors/add/', add_author, name='add_author'),
    # path('books/add/', add_book, name='add_book'),

    # New Authentication URL patterns
    path('register/', register, name='register'), # Your custom registration view
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='relationship_app:logout'), name='logout'),
    # Note: next_page for logout can also be set via settings.LOGOUT_REDIRECT_URL,
    # but explicitly setting it here to the logout template URL is also common.
]