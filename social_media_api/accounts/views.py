from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserRegistrationSerializer, UserSerializer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.get(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

class FollowUserView(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        user_to_follow = get_object_or_404(self.get_queryset(), pk=pk)
        if request.user == user_to_follow:
            return Response({'error': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
        
        request.user.following.add(user_to_follow)
        return Response({'status': 'You are now following this user.'}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        user_to_unfollow = get_object_or_404(self.get_queryset(), pk=pk)
        request.user.following.remove(user_to_unfollow)
        return Response({'status': 'You have unfollowed this user.'}, status=status.HTTP_200_OK)