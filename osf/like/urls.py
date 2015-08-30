from django.conf.urls import patterns, url, include
from views import *

urlpatterns = patterns( '',

    (r'do$', dolike),
    (r'undo$', undolike),
 )
