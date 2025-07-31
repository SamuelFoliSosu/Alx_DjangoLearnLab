from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    fields = '__all__'