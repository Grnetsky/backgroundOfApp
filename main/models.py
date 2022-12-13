from django.db import models
import uuid
# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    sex = models.BooleanField(default=True)
    head_portrait = models.ImageField(upload_to='head_portrait', verbose_name='头像',
                                      default='/head_portrait/head_portrait.jpg')

    class Meta:
        db_table = 'auth_user'
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
    # user_type = models.IntegerField(choices=((1,"超级用户"),(2,"普通用户")))


class Content(models.Model):
    title = models.CharField(max_length=20, verbose_name='标题')
    desc = models.CharField(max_length=256, default='')
    updateTime = models.DateTimeField(auto_now=True)
    content = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='contents')

    class Meta:
        db_table = 'article'
        verbose_name = '文章表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
