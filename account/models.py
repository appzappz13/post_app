from distutils.command.upload import upload
from pyexpat import model
from urllib import request
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    post_content = models.CharField(max_length=4000)
    post_time = models.DateTimeField(auto_now=True)
    post_like = models.IntegerField()
    post_comment = models.CharField(max_length=1000)
    post_image = models.ImageField(upload_to ='media/')


