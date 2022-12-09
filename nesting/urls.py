from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MyTestView.as_view(), name='nesting_comments'),
]