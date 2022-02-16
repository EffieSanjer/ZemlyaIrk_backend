from django.urls import path
from . import views

urlpatterns = [
    path('map', views.Roads.as_view(), name='map_roads'),
    path('map/<int:pk>', views.Road_Card.as_view(), name='road_item'),

]