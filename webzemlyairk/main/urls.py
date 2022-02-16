from django.urls import path
from . import views
from feedbacks.views import AddFeedback as f_views

urlpatterns = [
    path('', views.index, name='mainpage'),
    path('contacts', views.contacts, name='contact'),
    path('compare', views.Compare.as_view(), name='compare'),
    path('buy', views.buy, name='buy'),
    path('sell', views.sell, name='sell'),
    path('search', views.search, name='search'),
    path('buy_feedback', f_views.as_view(), name='add_buy_feedback'),
    path('sell_feedback', f_views.as_view(), name='add_sell_feedback'),
]