from django.urls import path, include
from . import views

urlpatterns = [
    path('user_1/', include('objects.login_urls')),
    # path('favourite/', include('objects.urls')),
    # path('my_objects/', include('objects.urls')),
    # # path('searches/', include('users.urls')),
    # path('user_1/info', include('users.urls')),
]