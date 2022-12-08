from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='posts_list'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('posts/<int:pk>/vote/', views.VoteCreate.as_view(), name='create_vote'),
]