from django.urls import path, include
from .api import PostAPI
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('posts', views.PostView)

urlpatterns = [
    path('', include(router.urls)),
    
]

