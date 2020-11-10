from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
#from core.views import TestView
from core.views import PostView,PostCreateView
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('admin/', admin.site.urls),
    #path('',TestView.as_view(),name='test'),
    path('',PostView.as_view(),name='test'),
    path('create/',PostCreateView.as_view(),name='create'),
    path('api/token/',obtain_auth_token,name='obtain_token')
]
