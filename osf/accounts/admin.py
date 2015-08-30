# coding=utf-8
from django.contrib import admin

from accounts.models import MyProfile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class ProfileInline( admin.StackedInline ):
    model = MyProfile
    # fk_name = 'user'
    max_num = 1
    can_delete = False

class CustomUserAdmin( UserAdmin ):
    inlines = [ProfileInline, ]
#     list_display = ( 'uid', 'utype', 'uname', 'citizenid', 'dep', 'chinesename', 'title', )  # display
admin.site.unregister( User )
admin.site.register( User, CustomUserAdmin )



