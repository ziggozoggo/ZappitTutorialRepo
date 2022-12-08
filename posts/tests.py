from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Post, Vote


class PostTestCase(TestCase):
    """Model Post test case
    """
    def setUp(self) -> None:
        self.user = User.objects.create(username='test_user_name')
        self.client.force_login(self.user)
        self.post = Post.objects.create(title='A post title', url='http://localhost:8000', poster=self.user)
    
    def test_post_content(self):
        self.assertEqual(self.post.title, 'A post title')
        self.assertEqual(self.post.url, 'http://localhost:8000')
        self.assertEqual(self.post.poster.username, 'test_user_name')

class VoteTestCase(TestCase):
    """Model Vote test case
    """
    def setUp(self) -> None:
        self.user = User.objects.create(username='test_user_name')
        self.client.force_login(self.user)
        self.post = Post.objects.create(title='A post title', url='http://localhost:8000', poster=self.user)
        self.vote = Vote.objects.create(voter=self.user, post=self.post)

    def test_vote_content(self):
        self.assertEqual(self.vote.post.title, 'A post title')
        self.assertEqual(self.vote.voter.username, 'test_user_name')