# notifications/serializers.py

from rest_framework import serializers
from .models import Notification
from accounts.serializers import UserSerializer
from posts.serializers import PostSerializer

class NotificationSerializer(serializers.ModelSerializer):
    actor = UserSerializer(read_only=True)
    # Use a SerializerMethodField for the target
    target = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'is_read', 'created_at', 'target']
        read_only_fields = ['recipient', 'actor', 'verb', 'is_read', 'created_at']

    def get_target(self, obj):
        if obj.target:
            # You might need to add other serializers here based on the target type
            if obj.content_type.model == 'post':
                return PostSerializer(obj.target).data
            return None
        return None