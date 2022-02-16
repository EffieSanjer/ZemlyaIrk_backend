from django.urls import path
from . import views

urlpatterns = [
    path('', views.RequestView.as_view(), name='all_requests'),
    path('my', views.MyRequestView.as_view(), name='my_requests'),
    path('client_<int:pk>', views.ClientRequestView.as_view(), name='client_requests'),
    path('emp_<int:pk>', views.EmpRequestView.as_view(), name='emp_requests'),
    path('add', views.AddReq.as_view(), name='add_req'),
    path('<int:pk>', views.Order_Card.as_view(), name='order_item'),
    path('<int:pk>/edit', views.EditReq.as_view(), name='edit_req'),
    path('<int:pk>/delete', views.DeleteReq.as_view(), name='delete_req'),
    path('<int:pk>/finish', views.FinishReq.as_view(), name='finish_req'),
    path('<int:pk>/stop', views.StopReq.as_view(), name='stop_req'),
    path('<int:pk>/continue', views.ContReq.as_view(), name='continue_req'),

    path('<int:order_id>/add_comm', views.AddComm.as_view(), name='add_comm_order'),
    path('<int:order_id>/delete_comm_<int:pk>', views.DeleteComm.as_view(), name='delete_comm_order'),
    
    path('<int:order_id>/delete_mem_<int:pk>', views.DeleteMember.as_view(), name='delete_member'),
    
]