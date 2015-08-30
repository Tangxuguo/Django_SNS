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
import  json
from django.shortcuts import get_object_or_404,get_list_or_404
from notification.models import *
from django.contrib.auth.models import User
from accounts.models import *
from like.models import *
from notification.models import *
from comment.models import *
from follow.models import *
from event.models import *
def create_post(request):
    if request.method == 'GET':
        notifications = get_all_notifications(request.user.id)
        t = get_template('post/create.html')
        c = RequestContext(request,locals())
        return HttpResponse(t.render(c))
    if request.method == 'POST':
        #1 save post
        post = Post.objects.create(author = request.user.id)
        title = request.POST['title']
        post.content = request.POST['content']
        if len(title)>0:
            print "title"
            post.title = title
        tags = request.POST['tags'].split(' ')
        for i in tags:
            tag,created = Tag.objects.get_or_create(name = i)
            post.tags.add(tag)
        post.save()
        #2 add event
        event = toEvent(Dic.OBJECT_TYPE_POST,post)
        #3 push follower

        #4 push to users who follow the tags in the post
        mydict = {"status":"105000"}
        return HttpResponse(json.dumps(mydict),content_type="application/json")

def get_post(request,id):
    notifications = get_all_notifications(request.user.id)
    post = get_object_or_404(Post, pk=id)
    u = User.objects.get(id = post.author)
    follow = Follow.objects.filter(followee = post.author ,follower = request.user).exists()
    is_like= Like.objects.filter(user_id=request.user.id,object_type = Dic.OBJECT_TYPE_POST,object_id = post.id).exists()
    comments = Comment.objects.filter( object_type = Dic.OBJECT_TYPE_POST, object_id=post.id).order_by("-ts")
    t=get_template('post/index.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def delete_post(request,id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    mydict = {"status":"105002"}
    return HttpResponse(json.dumps(mydict),content_type="application/json")

def view_post(request, id):
    product_instance = Post.objects.get(id = id)
    t=get_template('post/view_product.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_post(request, id):
    product_instance = Post.objects.get(id=id)
    t=get_template('post/edit_product.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def list_post(request):
    list_items = Post.objects.all()
    paginator = Paginator(list_items ,10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('post/list_product.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))
