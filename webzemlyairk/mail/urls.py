from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdminMess.as_view(), name='messages'),
    path('add', views.AddMess.as_view(), name='add_mess'),
    # path('<int:pk>', views.AdminRoad.as_view(), name='loc'),
    # path('<int:pk>/delete', views.DeleteRoad.as_view(), name='delete_mess'),
]