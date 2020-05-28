from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


from .models import Post

class PostSerializer(serializers.ModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name="posts:user-detail")
    author = serializers.SlugRelatedField(slug_field='username', queryset= User.objects.all())
    class Meta:
        model = Post
        fields = (
            'title', 'content', 'author',
        )