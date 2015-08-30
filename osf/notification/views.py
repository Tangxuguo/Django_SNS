#/usr/bin/python
#coding: utf8
from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse

from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from models import *

def comment(request):
    notis = Notification.objects.filter(notified_user = request.user.id).order_by("-ts")
    dic = Dic()
    comments_type = [Dic.NOTIFY_TYPE_COMMENT_REPLY,Dic.NOTIFY_TYPE_COMMENT]
    comments = notis.filter(notify_type__in=comments_type,status=0)
    comments.update(status=1)
    comment_counter = comments.count()
    like_counter = notis.filter(notify_type=Dic.NOTIFY_TYPE_LIKE,status=0).count()
    follow_counter = notis.filter(notify_type=Dic.NOTIFY_TYPE_FOLLOW,status=0).count()
    system_counter = notis.filter(notify_type=Dic.NOTIFY_TYPE_SYSTEM,status=0).count()
    notifications = {'comment':comment_counter,"like":like_counter,'follow':follow_counter,'system':system_counter}
    t=get_template('notification/comment.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def like(request):
    notis = Notification.objects.filter(notified_user = request.user.id).order_by("-ts")
    dic = Dic()
    comments_type = [Dic.NOTIFY_TYPE_COMMENT_REPLY,Dic.NOTIFY_TYPE_COMMENT]
    comment_counter = notis.filter(notify_type__in=comments_type,status=0).count()
    likes = notis.filter(notify_type=Dic.NOTIFY_TYPE_LIKE,status=0)
    likes.update(status=1)
    like_counter = likes.count()
    follow_counter = notis.filter(notify_type=Dic.NOTIFY_TYPE_FOLLOW,status=0).count()
    system_counter = notis.filter(notify_type=Dic.NOTIFY_TYPE_SYSTEM,status=0).count()
    notifications = {'comment':comment_counter,"like":like_counter,'follow':follow_counter,'system':system_counter}
    t=get_template('notification/like.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def follow(request):
    notis = Notification.objects.filter(notified_user = request.user.id).order_by("-ts")
    dic = Dic()
    comments_type = [Dic.NOTIFY_TYPE_COMMENT_REPLY,Dic.NOTIFY_TYPE_COMMENT]
    comment_counter = notis.filter(notify_type__in=comments_type,status=0).count()
    like_counter = notis.filter(notify_type=Dic.NOTIFY_TYPE_LIKE,status=0).count()
    follows = notis.filter(notify_type=Dic.NOTIFY_TYPE_FOLLOW,status=0)
    follows.update(status=1)
    follow_counter = follows.count()
    system_counter = notis.filter(notify_type=Dic.NOTIFY_TYPE_SYSTEM,status=0).count()
    notifications = {'comment':comment_counter,"like":like_counter,'follow':follow_counter,'system':system_counter}
    t=get_template('notification/follow.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def system(request):
    notis = Notification.objects.filter(notified_user = request.user.id).order_by("-ts")
    dic = Dic()
    comments_type = [Dic.NOTIFY_TYPE_COMMENT_REPLY,Dic.NOTIFY_TYPE_COMMENT]
    comment_counter = notis.filter(notify_type__in=comments_type,status=0).count()
    like_counter = notis.filter(notify_type=Dic.NOTIFY_TYPE_LIKE,status=0).count()
    follow_counter = notis.filter(notify_type=Dic.NOTIFY_TYPE_FOLLOW,status=0).count()
    systems = notis.filter(notify_type=Dic.NOTIFY_TYPE_SYSTEM,status=0)
    systems.update(status=1)
    system_counter = systems.count()
    notifications = {'comment':comment_counter,"like":like_counter,'follow':follow_counter,'system':system_counter}
    t=get_template('notification/system.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))
