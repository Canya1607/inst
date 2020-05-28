from django.urls import path, include
from .api import userProfileAPI
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('userProfiles', views.userProfileView)

urlpatterns = [
    path('', include(router.urls)),
    
]

# urlpatterns = [
#     path('<str:username', user_detail_view),
    
# ]
