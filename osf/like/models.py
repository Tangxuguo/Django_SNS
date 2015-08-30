#/usr/bin/python
#coding: utf8
from django.db import models
import datetime
# Create your models here.

class Like(models.Model):
    id = models.AutoField( primary_key = True )
    object_type = models.IntegerField()	#被通告的对象类型 Dic里有定义
    object_id = models.IntegerField()	#被通告对象的ID
    user_id = models.IntegerField()	#被通告的用户
    ts = models.DateTimeField( default = datetime.datetime.now() )	#通知时间戳