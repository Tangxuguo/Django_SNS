from django.db import models
from post.models import *
# Create your models here.

class ShortPost (models.Model):
    id = models.AutoField( primary_key = True )
    author = models.IntegerField()
    ts = models.DateTimeField( default = datetime.datetime.now() )
    content = models.TextField()
    title = models.CharField( max_length = 100,default="New Post" )
    excerpt = models.CharField( max_length = 100,blank=True, )
    status = models.IntegerField(default=0)
    comment_status = models.IntegerField(default=0)
    pwd = models.CharField( max_length = 100,blank=True, )
    lastts = models.DateTimeField( auto_now=True )
    like_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    url = models.URLField(blank=True,)
    tags = models.ManyToManyField( Tag,)
    album = models.IntegerField(default=0)
    cover = models.URLField(blank=True,)