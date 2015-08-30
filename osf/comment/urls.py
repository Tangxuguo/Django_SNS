from django.conf.urls import patterns, url, include
from views import *

urlpatterns = patterns( '',

    (r'^create$', create_comment),
    (r'^(?P<type>[^/]+)/(?P<id>[^/]+)/$', get_comments),
    (r'^attach/(?P<type>[A-Za-z]+)/(?P<id>[^/]+)/$', get_attachcomments),
    (r'^attach/(?P<type>[A-Za-z]+)/(?P<id>[^/]+)$', get_attachcomments),

 )
