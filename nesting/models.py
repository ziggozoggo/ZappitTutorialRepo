from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    author = models.ForeignKey(User, related_name='author_comment', on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.author}'s comment {self.datetime}"