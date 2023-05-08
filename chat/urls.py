from django.urls import path

from . import views
from .views import direct_chat_room

app_name = 'chat'

urlpatterns = [
    path('chat/', views.messaging_page, name='chat'),
    path('chat/chat_room/<str:room_name>/', views.chat_room, name='chat-room'),
    path('chat/direct_chat/<int:pk>/', views.direct_chat_room, name='direct-chat'),
]