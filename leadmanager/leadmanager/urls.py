
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from posts.views import feed_view, post_detail_view
from userProfiles.views import user_detail_view

# 

urlpatterns = [
    path('', include('posts.urls')), # main/posts
    path('', include('accounts.urls')),
    path('', include('userProfiles.urls')), # main/userProfiles
    path('posts/<int:post_id>', post_detail_view ),
    path('userProfiles/', user_detail_view),
    #path('profile/', include('userProfiles.urls')),
    path('admin/', admin.site.urls),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
