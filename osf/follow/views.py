#/usr/bin/python
#coding: utf8
from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse

from django.shortcuts import get_object_or_404

from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User

import json
from models import *
from notification.models import *
# Create your views here.

def dofollow(request,id):
    if request.method == 'POST':
        followee = get_object_or_404(User,pk=id)
        follow,created = Follow.objects.get_or_create(follower=request.user,followee=followee)
        follow.save()
        Notification.objects.create(notify_type = Dic.NOTIFY_TYPE_FOLLOW,
                                     notify_id=0,
                                     object_type=Dic.OBJECT_TYPE_USER,
                                     object_id=followee.id,
                                     notified_user=followee.id,
                                     notifier=request.user.id,
                                    notifier_name =request.user.username,
                                    notifier_avatar =request.user.get_profile().get_mugshot_url())
        mydict = {"status":"111000"}
        return HttpResponse(json.dumps(mydict),content_type="application/json")
def undofollow(request,id):
    if request.method == 'POST':
        followee = get_object_or_404(User,pk=id)
        get_object_or_404(Follow,follower=request.user,followee=followee).delete()
        mydict = {"status":"111001"}
        return HttpResponse(json.dumps(mydict),content_type="application/json")