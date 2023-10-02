from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<str:room>/', views.room, name="room"),
    path('checkview', views.checkview, name="checkview"),
    path('send', views.send, name="send"),
    path('getMessages/<str:room>/', views.getMessages, name="getMessages"),
    path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),

    # path('favicon.ico/', views.favicon, name='favicon'),
]