from django.conf import settings
from django.db import models
from django.utils import timesince, timezone
from user.models import User


class Post(models.Model):
    author = models.CharField(max_length=36)
    profile = models.TextField(null=True)
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)
    content = models.TextField()
    id_content = models.BigAutoField(primary_key=True,blank=True)

    like = models.ManyToManyField(User, related_name='likes', blank=True)
    like_count = models.IntegerField(default=0) 

    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    class Meta():
        db_table='Post'

class Comment(models.Model):
    Post = models.ForeignKey(Post,null=True,blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    class Meta():
        db_table='Comment'


# Create your models here.
