from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdminObjectView.as_view(), name='objects'),
    path('client_<int:pk>', views.ClientObjectView.as_view(), name='client_objects'),
    path('add', views.AddObj.as_view(), name='add_place'),
    path('<int:pk>', views.AdminPlaceView.as_view(), name='place'),
    path('<int:pk>/update', views.EditObj.as_view(), name='edit_place'),
    path('<int:pk>/delete', views.DeleteObj.as_view(), name='delete_place'),

    path('<int:obj_id>/add_comm', views.AddComm.as_view(), name='add_comm_object'),
    path('<int:obj_id>/delete_comm_<int:pk>', views.DeleteComm.as_view(), name='delete_comm_object'),

]