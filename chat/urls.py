from django.urls import path
from .views import Chathome, SearchView, onlineUsers
from . import views

from user import views as user_view
urlpatterns = [
   
    path('', views.Chathome, name='Chathome'),
    path('friend/<int:pk>', views.detail, name="detail"),
    path('sent_msg/<str:pk>', views.sentMessages, name = "sent_msg"),
    path('rec_msg/<str:pk>', views.receivedMessages, name = "rec_msg"),
    path('add/', views.addFriend, name = "add"),
    path('addf/<str:pk>', views.add, name = "addf"),
    path('online/', views.onlineUsers, name = "online"),
    path('search/', SearchView.as_view(), name='search'),
   
   
   
]