from django.conf.urls import patterns, url, include
from views import *

urlpatterns = patterns( '',

    (r'comment/$', comment),
    (r'follow/$', follow),
    (r'like/$', like),
    (r'system/$', system),

 )
