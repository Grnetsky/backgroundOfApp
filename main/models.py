from django.db import models
import uuid
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=30)
    sex = models.BooleanField(default=True)
    registerDate = models.DateTimeField(auto_now=True)
    # user_type = models.IntegerField(choices=((1,"超级用户"),(2,"普通用户")))
class Content(models.Model):
    title = models.CharField(max_length=20)
    updateTime = models.DateTimeField(auto_now=True)
    content = models.TextField()
    picture = models.ImageField(null=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE,related_name='contents')
