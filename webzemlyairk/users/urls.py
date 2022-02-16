from django.urls import path
from . import views

urlpatterns = [
    path('', views.users),
    path('clients', views.ClientsView.as_view(), name='all_clients'),
    path('clients/<int:pk>', views.ClientCard.as_view(), name='client_item'),
    path('clients/add', views.AddClient.as_view(), name='add_client'),
    path('clients/<int:pk>/edit', views.EditClient.as_view(), name='edit_client'),
    path('clients/<int:pk>/delete', views.DeleteClient.as_view(), name='delete_client'),
    path('clients/<int:client_id>/add_comm', views.AddComm.as_view(), name='add_comm_client'),
    path('clients/<int:client_id>/delete_comm_<int:pk>', views.DeleteComm.as_view(), name='delete_comm_client'),
###########
    path('team', views.TeamView.as_view(), name='all_emps'),
    path('team/<int:pk>', views.TeamCard.as_view(), name='emp_item'),
    path('team/add', views.AddEmp.as_view(), name='add_emp'),
    path('team/<int:pk>/edit', views.EditEmp.as_view(), name='edit_emp'),
    path('team/<int:pk>/delete', views.DeleteEmp.as_view(), name='delete_emp'),
    
]