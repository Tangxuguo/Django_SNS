# coding=utf-8
from django.db import models
import  datetime


NOTIFY_OBJECT_TYPE = {
    'NOTIFY_TYPE_SYSTEM':0,
    'NOTIFY_TYPE_COMMENT':1,
    'NOTIFY_TYPE_COMMENT_REPLY':2,
    'NOTIFY_TYPE_LIKE':3,
    'NOTIFY_TYPE_FOLLOW':4,
}

class Dic (object):
	OBJECT_TYPE_POST = 0
	OBJECT_TYPE_PHOTO = 1
	OBJECT_TYPE_ALBUM = 2
	OBJECT_TYPE_FOLLOWING = 3
	OBJECT_TYPE_SHORTPOST = 4
	OBJECT_TYPE_USER = 5

	NOTIFY_TYPE_SYSTEM = 0
	NOTIFY_TYPE_COMMENT = 1
	NOTIFY_TYPE_COMMENT_REPLY = 2
	NOTIFY_TYPE_LIKE = 3
	NOTIFY_TYPE_FOLLOW = 4

	object_type_post = 0
	object_type_photo = 1
	object_type_album = 2
	object_type_following = 3
	object_type_shortpost = 4

	notify_type_system = 0
	notify_type_comment = 1
	notify_type_comment_reply = 2
	notify_type_like = 3
	notify_type_follow = 4

# Create your models here.
class Notification (models.Model):

    id = models.AutoField( primary_key = True )
    notify_type = models.IntegerField()
    notify_id = models.IntegerField() #通告对象ID,如评论的ID
    object_type = models.IntegerField()	#被通告的对象类型 Dic里有定义
    object_id = models.IntegerField()	#被通告对象的ID
    notified_user = models.IntegerField()	#被通告的用户
    notifier = models.IntegerField()		#通告者
    ts = models.DateTimeField( default = datetime.datetime.now() )	#通知时间戳
    status = models.IntegerField(default=0)			#状态 0未读 1已读

    #以下属性用于通知展现
    notifier_name = models.CharField( max_length = 100,blank=True  )
    notifier_avatar =  models.URLField(blank=True )
    object_title = models.CharField( max_length = 100,blank=True )

def get_all_notifications(user_id):
	notis = Notification.objects.filter(notified_user = user_id).order_by("-ts")
	comments_type = [Dic.NOTIFY_TYPE_COMMENT_REPLY,Dic.NOTIFY_TYPE_COMMENT]
	comment_counter = notis.filter(notify_type__in=comments_type,status=0).count()
	like_counter = notis.filter(notify_type=Dic.NOTIFY_TYPE_LIKE,status=0).count()
	follows = notis.filter(notify_type=Dic.NOTIFY_TYPE_FOLLOW,status=0)
	follows.update(status=1)
	follow_counter = follows.count()
	system_counter = notis.filter(notify_type=Dic.NOTIFY_TYPE_SYSTEM,status=0).count()
	notifications = {'comment':comment_counter,"like":like_counter,'follow':follow_counter,'system':system_counter}
	return notifications