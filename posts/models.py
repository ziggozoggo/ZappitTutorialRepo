from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    """Post Model
    """
    title = models.CharField(max_length=100)
    url = models.URLField()
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Vote(models.Model):
    """Vote Model (one vote for user for one post)
    """
    voter = models.ForeignKey(User, related_name='voter_user', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='vote_post', on_delete=models.CASCADE)

    def __str__(self) -> str:
        voter = self.voter.username
        post = self.post.title
        return f'{voter} - {post}'