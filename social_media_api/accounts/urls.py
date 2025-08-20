# accounts/urls.py

from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserProfileView, FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/<str:username>/', UserProfileView.as_view(), name='profile'),
    path('follow/<int:pk>/', FollowUserView.as_view(), name='follow-user'),    # New URL
    path('unfollow/<int:pk>/', UnfollowUserView.as_view(), name='unfollow-user'), # New URL
]