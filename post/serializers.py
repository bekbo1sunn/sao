from rest_framework.serializers import ModelSerializer
from review.serializers import CommentSerializer

from .models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance:Post):
        rep = super().to_representation(instance)
        rep['likes'] = instance.likes.all().count()
        comments = instance.comments.all() # все комменты данного поста
        rep['comments'] = CommentSerializer(comments, many=True, context=self.context).data
        return rep        

