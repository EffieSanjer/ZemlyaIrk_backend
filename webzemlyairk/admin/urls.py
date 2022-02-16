from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='main_admin'),
    path('requests/', include('requests.urls')),
    path('users/', include('users.urls')),
    path('messages/', include('mail.urls')),
    path('feedbacks/', include('feedbacks.urls')),
    path('objects/', include('objects.admin_urls')),
    path('localities/', include('roads.admin_urls'))
]