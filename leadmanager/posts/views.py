from django.shortcuts import render
from .models import  Post
from rest_framework import viewsets
from .serializers import PostSerializer
from django.http import HttpResponse


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def feed_view(request, *args, **kwargs):
    return HttpResponse("<h1> Feeed page </h1>")

def post_detail_view(request,post_id ,*args, **kwargs):
    return HttpResponse(f"<h1> Post {post_id} </h1>")