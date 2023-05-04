from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from post.models import Post

from .models import Comment, Favorite, Like
from .permissions import IsAuthor
from .serializers import CommentSerializer, FavoriteSerializer, RatingSerializer


class CommentViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthor]


class FavoriteViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    

    

@api_view(['POST'])
def toggle_like(request, id):
    user = request.user
    if not user.is_authenticated:
        return Response(status=401)
    post = get_object_or_404(Post, id=id)
    if Like.objects.filter(user=user, post=post).exists():
        # Если лайк есть, то удаляем его
        Like.objects.filter(user=user, post=post).delete()
    else:
        # если нет, создаем
        Like.objects.create(user=user, post=post)
    return Response(status=201)


class AddRatingAPIView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(request_body=RatingSerializer())
    def post(self, request):
        ser = RatingSerializer(
            data=request.data, 
            context={"request":request}
            )
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status=201)
    