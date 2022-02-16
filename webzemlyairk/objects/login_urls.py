from django.urls import path
from . import views

urlpatterns = [

    path('favourite/', views.FavouriteView.as_view(), name='favourite'),
    path('my_objects/', views.MyObjectsView.as_view(), name='my_sales'),
]