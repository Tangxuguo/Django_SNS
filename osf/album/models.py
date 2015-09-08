# coding=utf-8
import datetime
from django.db import models
from tag.models import Tag
from django.contrib.auth.models import  User
# Create your models here.
from django.db.models.signals import post_save

class Photo (models.Model):
	id = models.AutoField( primary_key = True )
	key = models.CharField( max_length = 100,blank = True, )
	album_id = models.IntegerField(blank = True,default = 0)
	ts = models.DateTimeField( default = datetime.datetime.now() )
	desc = models.CharField( max_length = 200,blank = True, )


class Album (models.Model):
	id = models.AutoField( primary_key = True )
	user_id = models.IntegerField()
	create_ts = models.DateTimeField( default = datetime.datetime.now() )
	album_title = models.CharField( max_length = 100,default = 'New Album' )
	album_desc = models.CharField( max_length = 200,blank = True, )
	last_add_ts = models.DateTimeField( auto_now=True )
	photos_count = models.IntegerField(default=0)
	status = models.IntegerField(default=0)
	cover = models.URLField(default="http://7xjfbe.com1.z0.glb.clouddn.com/23.jpg")
	like_count = models.IntegerField(default=0)
	share_count = models.IntegerField(default=0)
	comment_count = models.IntegerField(default=0)
	photos = models.ManyToManyField( Photo )
	tags = models.ManyToManyField( Tag )