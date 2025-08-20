# posts/views.py

from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get the users that the current user is following
        followed_users = self.request.user.following.all()
        # Get posts from those users, ordered by creation date
        return Post.objects.filter(author__in=followed_users).order_by('-created_at')
    
class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        user = request.user
        like, created = Like.objects.get_or_create(user=user, post=post)
        if not created:
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        # Optionally, create a notification here
        # from notifications.models import Notification
        # from django.contrib.contenttypes.models import ContentType
        # content_type = ContentType.objects.get_for_model(post)
        # Notification.objects.create(
        #    recipient=post.author,
        #    actor=user,
        #    verb="liked",
        #    target=post
        # )

        return Response(status=status.HTTP_201_CREATED)