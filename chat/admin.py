from django.contrib import admin
from .models import ChatRoom, Message, PrivateChatRoom, PrivateMessage

# Register your models here.

admin.site.register(ChatRoom)
admin.site.register(PrivateChatRoom)
admin.site.register(Message)
admin.site.register(PrivateMessage)