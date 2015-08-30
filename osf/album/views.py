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
# Create your views here.
from models import *

import json
import time
from PIL import Image,ImageFile
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
import logging, os

from osf.settings import qiniu_access_key,qiniu_secret_key,qiniu_bucket_name,qiniu_bucket_domain
from osf.settings import MEDIA_PATH
import qiniu
from qiniu import BucketManager
from notification.models import *
from comment.models import *
from event.models import *
logger = logging.getLogger(__name__)


def create_postphoto(request):
    if request.method == 'POST':
        f = request.FILES["uploader_input"]
        parser = ImageFile.Parser()
        for chunk in f.chunks():
            parser.feed(chunk)
        img = parser.close()
        photo = Photo.objects.create()
        filename = str(photo.id)+'.jpg'
        photo.key = filename
        photo.save()
        path = MEDIA_PATH+'/'+filename
        img.save(path)
        try:
            q = qiniu.Auth(qiniu_access_key, qiniu_secret_key)
            key = filename
            localfile = path

            mime_type = "image/jpeg"
            params = {'x:a': 'a'}
            token = q.upload_token(qiniu_bucket_name, key)
            ret, info = qiniu.put_file(token, key, localfile, mime_type=mime_type, check_crc=True)
            #图片连接加上 v?时间  是因为七牛云缓存，图片不能很快的更新，用filename?v201504261312的形式来获取最新的图片
            #request.user.img = "http://7xjfbe.com1.z0.glb.clouddn.com/"+filename + "?v" + time.strftime('%Y%m%d%H%M%S')
            #request.user.save()
            print ret['key'],ret['hash']
            #验证上传是否错误
            if ret['key'] != key or ret['hash'] != qiniu.etag(localfile):
                logger.error(u'[UserControl]上传错误：[%s]' % request.user.username)
                return HttpResponse(u"上传错误",status=500)

            mydict = {"id":photo.id,"status":"107000","key":key, "link":qiniu_bucket_domain+key}
            return HttpResponse(json.dumps(mydict),content_type="application/json")

        except Exception as e:

            #验证上传是否错误
            if not os.path.exists(path):
                logger.error(u'[UserControl]用户上传出错:[%s]',request.user.username)
                return HttpResponse(u"上传错误",status=500)

            return HttpResponse(u"上传失败!\n")

def create_photo(request):
    if request.method == 'POST':
        f = request.FILES["uploader_input"]
        parser = ImageFile.Parser()
        for chunk in f.chunks():
            parser.feed(chunk)
        img = parser.close()
        photo = Photo.objects.create()
        filename = str(photo.id)+'.jpg'
        photo.key = filename
        photo.save()
        path = MEDIA_PATH+'/'+filename
        img.save(path)
        try:
            q = qiniu.Auth(qiniu_access_key, qiniu_secret_key)
            key = filename
            localfile = path

            mime_type = "image/jpeg"
            params = {'x:a': 'a'}
            token = q.upload_token(qiniu_bucket_name, key)
            ret, info = qiniu.put_file(token, key, localfile, mime_type=mime_type, check_crc=True)
            #图片连接加上 v?时间  是因为七牛云缓存，图片不能很快的更新，用filename?v201504261312的形式来获取最新的图片
            #request.user.img = "http://7xjfbe.com1.z0.glb.clouddn.com/"+filename + "?v" + time.strftime('%Y%m%d%H%M%S')
            #request.user.save()
            #print ret['key'],ret['hash']
            #验证上传是否错误
            if ret['key'] != key or ret['hash'] != qiniu.etag(localfile):
                logger.error(u'[UserControl]上传错误：[%s]' % request.user.username)
                return HttpResponse(u"上传错误",status=500)

            mydict = {"id":photo.id,"status":"107000","key":key}
            return HttpResponse(json.dumps(mydict),content_type="application/json")

        except Exception as e:
            #验证上传是否错误
            if not os.path.exists(path):
                logger.error(u'[UserControl]用户上传出错:[%s]',request.user.username)
                return HttpResponse(u"上传错误",status=500)

            return HttpResponse(u"上传失败!\n")


def delete_photo(request, photo_id):
    if request.method == 'GET':
        print(photo_id)
        photo = get_object_or_404(Photo,pk = photo_id)
        try:
            bucket_name = qiniu_bucket_name
            key = photo.key
            print key
            q = qiniu.Auth(qiniu_access_key, qiniu_secret_key)
            bucket = BucketManager(q)
            ret, info = bucket.delete(bucket_name, key)
            print ret,info
            assert ret is not None
            photo.delete()
            mydict = {"status":"107002"}
            return HttpResponse(json.dumps(mydict),content_type="application/json")
        except Exception as e:
            logger.error(u'[UserControl]用户上传出错:[%s]',request.user.username)
            return HttpResponse(u"上传错误",status=500)


def create_photo_album(request,album_id):
    if request.method == 'POST':

        f = request.FILES["uploader_input"]
        parser = ImageFile.Parser()
        for chunk in f.chunks():
            parser.feed(chunk)
        img = parser.close().resize((100, 100),Image.ANTIALIAS)
        photo = Photo.objects.create()
        photo.save()
        # 在img被保存之前，可以进行图片的各种操作，在各种操作完成后，在进行一次写操作
        path = str(photo.id)+'.jpg'
        filename = path
        img.save(MEDIA_PATH+path)
        #选择上传头像到七牛还是本地
        try:
	        #上传头像到七牛
            from osf.settings import qiniu_access_key,qiniu_secret_key,qiniu_bucket_name
            import qiniu

            assert qiniu_access_key and qiniu_secret_key and qiniu_bucket_name
            q = qiniu.Auth(qiniu_access_key, qiniu_secret_key)

            key = filename
            localfile = path

            mime_type = "text/plain"
            params = {'x:a': 'a'}

            token = q.upload_token(qiniu_bucket_name, key)
            ret, info = qiniu.put_file(token, key, localfile, mime_type=mime_type, check_crc=True)

            #图片连接加上 v?时间  是因为七牛云缓存，图片不能很快的更新，用filename?v201504261312的形式来获取最新的图片
            request.user.img = "http://7xjfbe.com1.z0.glb.clouddn.com/"+filename + "?v" + time.strftime('%Y%m%d%H%M%S')
            request.user.save()
            #print ret['key'],ret['hash']
            #验证上传是否错误
            if ret['key'] != key or ret['hash'] != qiniu.etag(localfile):
                logger.error(u'[UserControl]上传错误：[%s]' % request.user.username)
                return HttpResponse(u"上传错误",status=500)

            mydict = {"id":photo.id,"status":"107000","key":key}
            return HttpResponse(json.dumps(mydict),content_type="application/json")

        except Exception as e:

            #验证上传是否错误
            if not os.path.exists(path):
                logger.error(u'[UserControl]用户上传出错:[%s]',request.user.username)
                return HttpResponse(u"上传错误",status=500)

            return HttpResponse(u"上传成功!\n(注意有10分钟缓存)")

def delete_photo_album(request,album_id,photo_id):
    if request.method == 'POST':

        f = request.FILES["uploader_input"]
        parser = ImageFile.Parser()
        for chunk in f.chunks():
            parser.feed(chunk)
        img = parser.close().resize((100, 100),Image.ANTIALIAS)
        photo = Photo.objects.create()
        photo.save()
        # 在img被保存之前，可以进行图片的各种操作，在各种操作完成后，在进行一次写操作
        path = str(photo.id)+'.jpg'
        filename = path
        img.save(path)
        #选择上传头像到七牛还是本地
        try:
	        #上传头像到七牛
            from osf.settings import qiniu_access_key,qiniu_secret_key,qiniu_bucket_name
            import qiniu

            assert qiniu_access_key and qiniu_secret_key and qiniu_bucket_name
            q = qiniu.Auth(qiniu_access_key, qiniu_secret_key)

            key = filename
            localfile = path

            mime_type = "image/jpeg"
            params = {'x:a': 'a'}

            token = q.upload_token(qiniu_bucket_name, key)
            ret, info = qiniu.put_file(token, key, localfile, mime_type=mime_type, check_crc=True)

            #图片连接加上 v?时间  是因为七牛云缓存，图片不能很快的更新，用filename?v201504261312的形式来获取最新的图片
            request.user.img = "http://7xjfbe.com1.z0.glb.clouddn.com/"+filename + "?v" + time.strftime('%Y%m%d%H%M%S')
            request.user.save()
            #print ret['key'],ret['hash']
            #验证上传是否错误
            if ret['key'] != key or ret['hash'] != qiniu.etag(localfile):
                logger.error(u'[UserControl]上传错误：[%s]' % request.user.username)
                return HttpResponse(u"上传错误",status=500)

            mydict = {"id":photo.id,"status":"107000","key":key}
            return HttpResponse(json.dumps(mydict),content_type="application/json")

        except Exception as e:

            #验证上传是否错误
            if not os.path.exists(path):
                logger.error(u'[UserControl]用户上传出错:[%s]',request.user.username)
                return HttpResponse(u"上传错误",status=500)

            return HttpResponse(u"上传失败!\n")

def upload_index(request):
    notifications = get_all_notifications(request.user.id)
    if request.method == 'GET':
        csrf_token = get_token(request)
        t = get_template('album/create_album.html')
        c = RequestContext(request,locals())
        return HttpResponse(t.render(c))

def create_album(request):
    if request.is_ajax():
        if request.method == 'POST':
            #try:
            print 'Raw Data: "%s"' % request.body
            data = json.loads(request.body.decode("utf-8"))
            album = Album.objects.create(user_id = request.user.id)
            album.album_desc=data["album_desc"]
            for i in data["photos"]:
                print i["id"],i["desc"]
                photo = get_object_or_404(Photo,pk=i["id"])
                photo.desc = i["desc"]
                photo.save()
                album.photos.add(photo)
            for i in data["tags"]:
                tag,created = Tag.objects.get_or_create(name = i)
                album.tags.add(tag)
            album.save()
            event = toEvent(Dic.OBJECT_TYPE_ALBUM,album)
            mydict = {"status":"106000"}
            return HttpResponse(json.dumps(mydict),content_type="application/json")
            # except:
            #     logger.error(u'[UserControl]创建相册出错:[%s]',request.user.username)
            #     return HttpResponse(u"上传错误",status=500)

def delete_album(request, album_id):
    if request.method == 'GET':
        csrf_token = get_token(request)
        t = get_template('album/create_album.html')
        c = RequestContext(request,locals())
        return HttpResponse(t.render(c))
    if request.method == 'POST':
        t = get_template('album/create_album.html')
        c = RequestContext(request,locals())
        return HttpResponse(t.render(c))

def view_album(request, id):
    notifications = get_all_notifications(request.user.id)
    img_base_url = qiniu_bucket_domain
    album = Album.objects.get(id=id)
    photos_id = album.photos.first().id
    comments = Comment.objects.filter( object_type = Dic.OBJECT_TYPE_PHOTO, object_id=photos_id).order_by("-ts")
    u = User.objects.get(id=album.user_id)
    product_instance = Album.objects.get(id = id)
    t=get_template('album/index.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))


def edit_album(request, id):
    product_instance = Album.objects.get(id=id)
    t=get_template('album/edit_album.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def list_album(request):
    list_items = Album.objects.all()
    paginator = Paginator(list_items ,10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('album/list_album.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))