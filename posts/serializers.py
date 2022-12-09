import json
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Vote


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class VoteSerializer(serializers.ModelSerializer):
    """Vote model serializer
    """
    class Meta:
        model = Vote
        fields = ['id']


class PostSerializer(serializers.ModelSerializer):
    """Post model serializer
    """
    poster = serializers.ReadOnlyField(source='poster.username')
    poster_id = serializers.ReadOnlyField(source='poster.id')

    # Количество votes
    votes  = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'poster','poster_id', 'created', 'votes']

    
    # Название функции после get_ должно совпадать 
    # с переменной serializers.SerializerMethodField()
    def get_votes(self, post: Post) -> int:
        votes_count = Vote.objects.filter(post=post).count()
        return votes_count


# Не работает!
class VotersSerializator(serializers.ModelSerializer):
    user = UserSerializer(many=True)
    class Meta:
        model = Vote
        fields = ['id', 'voter', 'user']


# Данные поста со списком "votes"
class PostDetailSerializer(serializers.ModelSerializer):
    """Post detail model serializer
    """
    poster = serializers.ReadOnlyField(source='poster.username')
    poster_id = serializers.ReadOnlyField(source='poster.id')

    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'poster','poster_id', 'created', 'vote_post']
        depth = 1


class NestedSerializer(serializers.ModelSerializer):
    voters = VoteSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'voters']
