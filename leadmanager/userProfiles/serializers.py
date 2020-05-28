
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