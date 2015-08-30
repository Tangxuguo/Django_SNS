from django.conf.urls import patterns, url, include
from views import *

urlpatterns = patterns( '',
    (r'^setting/info$', settingInfoPage),
     (r'^setting/avatar$', settingAvatar),
     (r'^setting/security$', settingSecurity),
    (r'^setting/changepw', resetpwdPage),
    (r'^setting/changeavatar', changeavatar),
 )
