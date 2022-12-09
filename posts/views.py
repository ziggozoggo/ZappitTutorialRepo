from rest_framework.reverse import reverse, reverse_lazy
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, permissions, mixins, status
from rest_framework.exceptions import ValidationError
from .serializers import PostSerializer, VoteSerializer, PostDetailSerializer
from .models import Post, Vote


@api_view(['GET'])
def api_root(request, format=None):
    res = Response({
        'List of posts': reverse('posts_list', request=request, format=format),
        'Post Detail <int:pk>': reverse('post_detail', request=request, format=format, kwargs={'pk': 1}),
        'Post Vote <int:pk>/vote': reverse('create_vote', request=request, format=format, kwargs={'pk': 1}),
    })

    return res

# Create your views here.
class PostList(generics.ListCreateAPIView):
    """Post list API view
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # Доступ к API на запись только авторизованным пользователям
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Переопределение (расширение ?) метода родительского класса
        При сохранении данных в модель описываем как создаём запись в обязательном
        поле poster - это экземпляр класса User владельца сессии
        """
        serializer.save(poster=self.request.user)

class VoteCreate(generics.CreateAPIView, mixins.DestroyModelMixin):
    """Vote create API view
    """
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Кверисет на все объекты нас не устраивает; определяем свои ограничения
        """
        user = self.request.user
        post = Post.objects.get(id=self.kwargs['pk']) # забираем pk из url
        res_query = Vote.objects.filter(voter=user, post=post)
        return res_query

    def perform_create(self, serializer):
        # Голосовать можно только один раз
        if self.get_queryset().exists():
            # raise выводится API
            raise ValidationError('You have already voted for this post')
        post = Post.objects.get(id=self.kwargs['pk'])
        serializer.save(voter=self.request.user, post=post)

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('You never voted for this post')


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        post = Post.objects.filter(id=kwargs['pk'], poster=self.request.user)
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('You are not owner of post')








