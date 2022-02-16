from django.urls import path
from . import views

urlpatterns = [
    path('', views.FeedbacksView.as_view(), name='feedbacks'),
    path('check_<int:pk>', views.CheckFeedback.as_view(), name='check_feedback'),
    # path('clients/add', views.AddClient.as_view(), name='add_client'),
    # path('<int:pk>/delete', views.DeleteClient.as_view(), name='delete_client'),
    
]