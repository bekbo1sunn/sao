from django.db import models
from account.models import User
from post.models import Post


class Comment(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='comments'
        )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Rating(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    value = models.IntegerField(
        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    )


    
class Favorite(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='favorites'
        )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='favorites'
    )

class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
