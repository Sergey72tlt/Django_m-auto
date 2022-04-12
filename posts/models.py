from django.db import models
from django.contrib.auth.models import User


def user_post_image_path(instance, filename):
    user_id = instance.author.id
    return f'user_{user_id}/posts/{filename}'


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_post_image_path)
    description = models.TextField(max_length=1000, blank=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, blank=True, related_name='like_posts')

    @property
    def likes_count(self):
        return self.likes.count()

    def __str__(self):
        return f'post {self.id}, author {self.author.username}'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Author - {self.author.username}, publicated - {self.date_pub}, post - {self.post.description[:15]}'