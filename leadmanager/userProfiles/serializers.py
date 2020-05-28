
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
 

from .models import userProfile

class userProfileSerializer(serializers.ModelSerializer):
    
    user = serializers.SlugRelatedField(slug_field='username', queryset= User.objects.all())
    class Meta:
        model = userProfile
        fields = (
            'user', 'image',
        )
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        return user
