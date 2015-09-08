# -*- coding: utf-8 -*-
from django.db import models
import  datetime
from tag.models import *
# Create your models here.
from django.core.cache import cache
from album.models import *
from notification.models import *
from follow.models import *
from post.models import *
from spost.models import *
class Event (models.Model):
    id = models.AutoField( primary_key = True )
    object_type = models.IntegerField(default=0  )
    object_id = models.IntegerField(default=0 )
    ts = models.DateTimeField( default = datetime.datetime.now() )	#通知时间戳
    user_id = models.CharField( max_length = 100,blank=True, )
    user_name = models.CharField( max_length = 100,blank=True, )
    user_avatar = models.CharField( max_length = 100,blank=True, )
    like_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    title = models.CharField( max_length = 100,blank=True, )
    summary = models.CharField( max_length = 1000,blank=True, )
    content = models.CharField( max_length = 10000,blank=True, )
    photos = models.ManyToManyField( Photo,)
    tags = models.ManyToManyField( Tag,)
    following_user_id = models.IntegerField(default=0)
    following_user_name = models.CharField( max_length = 200,blank=True,  )
    follower_user_id = models.IntegerField(default=0 )
    follower_user_name = models.CharField( max_length = 200,blank=True,  )
    is_like = models.BooleanField(default=False)

def toEvent(object_type, obj):
    #save event
    event = Event.objects.create()
    if Dic.OBJECT_TYPE_POST == object_type:
        event.object_type = Dic.OBJECT_TYPE_POST
        event.object_id = obj.id
        event.user_id = obj.author
        event.title = obj.title
        event.summary = obj.excerpt
        event.content = obj.cover
        event.like_count = obj.like_count
        event.share_count = obj.share_count
        event.comment_count = obj.comment_count
        event.tags = obj.tags.all()

    elif Dic.OBJECT_TYPE_ALBUM == object_type:
        event.object_type = Dic.OBJECT_TYPE_ALBUM
        event.object_id = obj.id
        event.user_id = obj.user_id
        event.title = obj.cover
        event.summary = obj.album_desc
        event.photos = obj.photos.all()
        event.content = obj.cover
        event.like_count = obj.like_count
        event.share_count = obj.share_count
        event.comment_count = obj.comment_count
        event.tags = obj.tags.all()
    elif Dic.OBJECT_TYPE_PHOTO == object_type:
        pass
    elif Dic.OBJECT_TYPE_SHORTPOST == object_type:
        event.object_type = Dic.OBJECT_TYPE_SHORTPOST
        event.object_id = obj.id
        event.user_id = obj.author
        event.summary = obj.content
        event.like_count = obj.like_count
        event.share_count = obj.share_count
        event.comment_count = obj.comment_count
    u = User.objects.get(id = event.user_id)
    event.user_name = u.username
    event.user_avatar = u.get_profile().get_mugshot_url()
    event.save()
    #push me
    feeds_event = cache.get("feed:user:"+str(event.user_id),[])
    feeds_event.append(event.id)
    cache.set("feed:user:"+str(event.user_id),feeds_event)
    #push to follower
    followers = User.objects.filter(follower__followee = u )
    for follower in followers:
        feeds_event = cache.get("feed:user:"+str(follower.id),[])
        feeds_event.append(event.id)
        cache.set("feed:user:"+str(follower.id),feeds_event)
    return event
def getFeeds(user_id):
    feeds_event=cache.get("feed:user:"+str(user_id),[])
    feeds = Event.objects.filter(id__in=feeds_event).order_by("-ts")
    for feed in feeds.all():
        if feed.object_type == Dic.OBJECT_TYPE_POST:
            t = Post.objects.get(pk=feed.object_id)
            feed.like_count = t.like_count
            feed.comment_count = t.comment_count
            print feed.like_count,feed.comment_count
        if feed.object_type == Dic.OBJECT_TYPE_ALBUM:
            t = Album.objects.get(pk=feed.object_id)
            feed.like_count = t.like_count
            feed.comment_count = t.comment_count
        if feed.object_type == Dic.OBJECT_TYPE_SHORTPOST:
            t = ShortPost.objects.get(pk=feed.object_id)
            feed.like_count = t.like_count
            feed.comment_count = t.comment_count
        feed.save()
    return feeds