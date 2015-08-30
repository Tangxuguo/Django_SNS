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
from event.models import *
import  json
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder

def create_spost(request):
    if request.method == 'GET':
        t = get_template('spost/create.html')
        c = RequestContext(request,locals())
        return HttpResponse(t.render(c))
    if request.method == 'POST':
        spost = ShortPost.objects.create(author = request.user.id)
        spost.content = request.POST['content']
        spost.save()
        event = toEvent(Dic.OBJECT_TYPE_SHORTPOST,spost)
        mydict = {"status":"105000","spost":model_to_dict(spost),"author_name":request.user.username,"avatar":request.user.get_profile().get_mugshot_url()}
        #mydict["spost"]=model_to_dict(spost)
        return HttpResponse(json.dumps(mydict,cls=DjangoJSONEncoder),content_type="application/json")

def view_spost(request, id):
    product_instance = ShortPost.objects.get(id = id)
    t=get_template('spost/view_product.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_spost(request, id):
    product_instance = ShortPost.objects.get(id=id)
    t=get_template('spost/edit_product.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def list_spost(request):
    list_items = ShortPost.objects.all()
    paginator = Paginator(list_items ,10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('spost/list_product.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))
