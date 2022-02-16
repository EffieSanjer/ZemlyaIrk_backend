from django.urls import path
from . import views

urlpatterns = [
    path('', views.objects),
    path('country_places/', views.ObjectView.as_view(), name='country'),
    path('country_places/<int:pk>', views.Place_Card.as_view(), name='place_item'),

]