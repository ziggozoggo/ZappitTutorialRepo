from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import UserSerializer, CommentSerializer, UserSecondSerializer
from .models import Comment, User

# Create your views here.

class CommentView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class UsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSecondSerializer

class UsersViewSimple(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class MyTestView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSecondSerializer

