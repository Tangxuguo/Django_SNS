from django.conf.urls import patterns, url, include
from views import *

urlpatterns = patterns( '',
    (r'^(?P<id>[^/]+)$', dofollow),
    (r'^undo/(?P<id>[^/]+)$', undofollow),
 )
