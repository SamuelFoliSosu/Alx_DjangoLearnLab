# posts/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView, LikeView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
    path('posts/<int:pk>/like/', LikeView.as_view(), name='like-post'),
    path('posts/<int:pk>/unlike', LikeView.as_view(), name='unlike-post'),
    path('', include(router.urls)), 
]