from django.conf.urls import patterns, url, include
from views import *

urlpatterns = patterns( '',
    (r'^create/$', create_post),
    (r'^list/$', list_post ),
    (r'^edit/(?P<id>[^/]+)/$', edit_post),
    (r'^view/(?P<id>[^/]+)/$', view_post),
 )
