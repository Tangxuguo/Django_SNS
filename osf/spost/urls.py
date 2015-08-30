from django.conf.urls import patterns, url, include
from views import *

urlpatterns = patterns( '',
    (r'^create$', create_spost),
    (r'^list/$', list_spost ),
    (r'^edit/(?P<id>[^/]+)/$', edit_spost),
    (r'^view/(?P<id>[^/]+)/$', view_spost),
 )
