from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdminRoads.as_view(), name='localities'),
    path('add', views.AddRoad.as_view(), name='add_loc'),
    path('<int:pk>', views.AdminRoad.as_view(), name='loc'),
    path('<int:pk>/update', views.EditRoad.as_view(), name='edit_loc'),
    path('<int:pk>/delete', views.DeleteRoad.as_view(), name='delete_loc'),
]