# accounts/serializers.py

from rest_framework import serializers
from rest_framework.authtoken.models import Token # New Import
from django.contrib.auth import get_user_model # New Import

User = get_user_model() # This is the preferred way to get the user model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'following']
        read_only_fields = ['followers', 'following']

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'bio']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
        )
        Token.objects.create(user=user)
        return user