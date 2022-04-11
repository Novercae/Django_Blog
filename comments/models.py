from django.db import models
from posts.models import Post
from django.contrib.auth.models import User

class Comment(models.Model):
    name_comment = models.CharField(max_length=100, verbose_name='Name')
    email_comment = models.EmailField(verbose_name='Email')
    comment = models.TextField(verbose_name='Comment')
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')
    user_comment = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='User')
    date_comment = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    published_comment = models.BooleanField(default=False, verbose_name='Published')

    def __str__(self):
        return self.name_comment