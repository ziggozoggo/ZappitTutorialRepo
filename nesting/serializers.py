# https://testdriven.io/blog/drf-serializers/#nested-serializers
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


# Через параметр depth (бежит по связям Foreign Key)
class CommentSerializer(serializers.ModelSerializer):
    # Поле, по которому вызываем сериализатор, должно быть в модели !
    # author = UserSerializer()
    class Meta:
        model = Comment
        fields = '__all__'
        depth = 1

# Через определение серилазитора для поля модели
class CommentSecondSerializer(serializers.ModelSerializer):
    # Поле, по которому вызываем сериализатор, должно быть в модели !
    author = UserSerializer()
    class Meta:
        model = Comment
        fields = '__all__'

# Reverse relations
# https://www.django-rest-framework.org/api-guide/relations/#reverse-relations
# author_comment - related_name модели Comments
# deth - позволяет вывести содержимое связанной модели
class UserSecondSerializer(serializers.ModelSerializer):   
    class Meta:
        model = User
        fields = ['id', 'username', 'author_comment']
        depth = 1
