# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse

from django.shortcuts import get_object_or_404
# Create your views here.
from models import *


# def saveFollower(request, user_id):
#     data = {'valid': False}
#     tl = Follower.objects.get(user_id=user_id)
#     if tl.created_by != request.user:
#         return render_json_response(data)
#     if request.method == "POST":
#         username = request.POST.get('username', '')
#         try:
#             user = User.objects.get(username=username)
#             if user.has_perm('collaborator', tl):
#                 data['info'] = u'用户 "%s" 已经添加过' % username
#                 return render_json_response(data)
#         except:
#             data['info'] = u'用户 "%s" 不存在' % username
#             return render_json_response(data)
#         assign('collaborator', user, tl)
#         return render_json_response({'valid': True,
#             'obj': {'pk': user.pk, 'username': user.username},
#             'html': render_string(COLLABORATOR_ROW_TMPL, {'o': user})
#             })
#     return render_json_response(data)
#
# def delFollower(request, user_id):
#
# def getFollowings(request):
# def getFollowers(request):
#def hasFollowing(int user_a, int user_b);
#def hasFollower(int user_a, int user_b);

def settingInfoPage(request):
    t = get_template('account/setting/info.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))
def settingAvatar(request):
    t = get_template('account/setting/avatar.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))
def settingSecurity(request):
    t = get_template('account/setting/security.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))
def resetpwdPage(request):
    t = get_template('account/setting/security.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))
def changeavatar(request):
    t = get_template('account/setting/security.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))
