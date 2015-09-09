#/usr/bin/python
#coding: utf8
from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse

from django.shortcuts import render,get_object_or_404
from django.views.generic import View
# Create your views here.
from models import *
from notification.models import *
import json
from accounts.models import MyProfile
from tag.models import Tag
from post.models import Post
from album.models import Album,Photo
from notification.models import *
from comment.models import Comment
from like.models import *
from spost.models import *
def get_comment(request):
    t = get_template('comment/index.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def create_comment(request):
    if request.method=='POST':
        object_type = int(request.POST['object_type'])
        object_id = int(request.POST['object_id'])
        content = request.POST['content']
        parent = int(request.POST['parent'])

        if object_type == Dic.OBJECT_TYPE_POST:
            object_title = Post.objects.get(pk=object_id).title
        if object_type == Dic.OBJECT_TYPE_ALBUM:
            object_title = Album.objects.get(pk=object_id).album_title
        if object_type == Dic.OBJECT_TYPE_SHORTPOST:
            object_title = ShortPost.objects.get(pk=object_id).content
        # this comment author
        author = request.user
         # get object author
        if object_type == Dic.OBJECT_TYPE_POST:
             object_author_id = Post.objects.get(pk=object_id).author
        if object_type == Dic.OBJECT_TYPE_ALBUM:
            object_author_id = Album.objects.get(pk=object_id).user_id
        if object_type == Dic.OBJECT_TYPE_SHORTPOST:
            object_author_id = ShortPost.objects.get(pk=object_id).author
        object_author = User.objects.get(pk=object_author_id)
        if parent>0:
            # parent comment author
            parent_author = get_object_or_404(Comment,pk=parent).author.id
            comment = Comment.objects.create(object_type=object_type, object_id=object_id,content=content,parent=parent,author=author,parent_author=object_author)
            notification = Notification.objects.create(notify_type = Dic.NOTIFY_TYPE_COMMENT,
                                     notify_id=comment.id,
                                     object_type=object_type,
                                     object_id=object_id,
                                     notified_user=parent_author,
                                     notifier=request.user.id,
                                     notifier_name =request.user.username,
                                     notifier_avatar =request.user.get_profile().get_mugshot_url(),
                                     object_title = object_title)
            notification.save()
            notification = Notification.objects.create(notify_type = Dic.NOTIFY_TYPE_COMMENT,
                                     notify_id=comment.id,
                                     object_type=object_type,
                                     object_id=object_id,
                                     notified_user=object_author.id,
                                     notifier=request.user.id,
                                     notifier_name =request.user.username,
                                     notifier_avatar =request.user.get_profile().get_mugshot_url(),
                                     object_title = object_title)
            notification.save()
        elif parent == 0:
            comment = Comment.objects.create(object_type=object_type, object_id=object_id,content=content,parent=parent,author=author,parent_author=object_author)
            notification = Notification.objects.create(notify_type = Dic.NOTIFY_TYPE_COMMENT,
                                     notify_id=comment.id,
                                     object_type=object_type,
                                     object_id=object_id,
                                     notified_user=object_author.id,
                                     notifier=request.user.id,
                                     notifier_name =request.user.username,
                                     notifier_avatar =request.user.get_profile().get_mugshot_url(),
                                     object_title = object_title                 )
            notification.save()





        mydict = {"status":"108000","avatar":author.get_profile().get_mugshot_url(),"author_id":author.id,"author_name":author.username}
        return HttpResponse(json.dumps(mydict),content_type="application/json")

def get_comments(request,type,id):
    print type,id
    if type == 'photo':
        comments = Comment.objects.filter( object_type = Dic.OBJECT_TYPE_PHOTO, object_id=id).order_by("-ts")
    if type == 'post':
        comments = Comment.objects.filter( object_type = Dic.OBJECT_TYPE_POST, object_id=id).order_by("-ts")
    t = get_template('comment/index.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def get_attachcomments(request,type,id):
    if type == 'photo':
        comments = Comment.objects.filter( object_type = Dic.OBJECT_TYPE_PHOTO, object_id=id).order_by("-ts")
    if type == 'post':
        comments = Comment.objects.filter( object_type = Dic.OBJECT_TYPE_POST, object_id=id).order_by("-ts")
    if type == 'spost':
        comments = Comment.objects.filter( object_type = Dic.OBJECT_TYPE_SHORTPOST, object_id=id).order_by("-ts")
    t = get_template('comment/attach_comments.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))
