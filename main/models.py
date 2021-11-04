from django.db import models
import uuid
# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    sex = models.BooleanField(default=True)
    class Meta:
        db_table='auth_user'
        verbose_name='用户管理'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.username
    # user_type = models.IntegerField(choices=((1,"超级用户"),(2,"普通用户")))


class Content(models.Model):
    title = models.CharField(max_length=20)
    updateTime = models.DateTimeField(auto_now=True)
    content = models.TextField()
    picture = models.ImageField(null=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='contents')
