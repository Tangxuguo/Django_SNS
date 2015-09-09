# coding=utf-8
from django.db import models
import datetime
from tag.models import Tag
# Create your models here.
from django.db.models.signals import post_save

from comment.models import *
from like.models import *

from notification.models import *

class Post (models.Model):
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

def update_comment_on_post(sender, instance, created, **kwargs):
    if created:
        if instance.object_type == Dic.OBJECT_TYPE_POST:
            t = Post.objects.get(pk=instance.object_id)
            t.comment_count += 1
            t.save()
def update_like_on_post(sender, instance, created, **kwargs):
    if created:
        if instance.object_type == Dic.OBJECT_TYPE_POST:
            t = Post.objects.get(pk=instance.object_id)
            t.like_count += 1
            t.save()
post_save.connect(update_comment_on_post, sender=Comment)
post_save.connect(update_like_on_post, sender=Like)
