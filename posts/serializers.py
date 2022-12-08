import json
from rest_framework import serializers
from .models import Post, Vote

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

class VoteSerializer(serializers.ModelSerializer):
    """Vote model serializer
    """
    class Meta:
        model = Vote
        fields = ['id']