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

def create_post(request):
    t = get_template('post/create_product.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def view_post(request, id):
    product_instance = Tag.objects.get(id = id)
    t=get_template('post/view_product.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_post(request, id):
    product_instance = Tag.objects.get(id=id)
    t=get_template('post/edit_product.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def list_post(request):
    list_items = Tag.objects.all()
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