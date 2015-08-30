from django.conf.urls import patterns, url, include
from views import *

urlpatterns = patterns( '',

    (r'^create$', create_album),
    (r'^list/$', list_album ),
    (r'^edit/(?P<id>[^/]+)/$', edit_album),
    (r'^view/(?P<id>[^/]+)/$', view_album),

    (r'^upload/$', upload_index),
    (r'^upload/photo$', create_photo),
    (r'^upload/postphoto$', create_postphoto),
    (r'^delete/photo/(?P<photo_id>[^/]+)/$', delete_photo),
    (r'^(?P<album_id>[^/]+)/upload/photo$', create_photo_album),
    (r'^(?P<album_id>[^/]+)/delete/photo/(?P<photo_id>[^/]+)/$', create_photo_album),
    (r'^(?P<id>[^/]+)/photos$', view_album),

 )
