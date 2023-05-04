from django.contrib import admin
from .models import Comment, Favorite, Like, Rating


admin.site.register(Comment)
admin.site.register(Favorite)
admin.site.register(Like)
admin.site.register(Rating)
