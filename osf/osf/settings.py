# -*- coding: utf-8 -*-
# Django settings for osf project.
import os
import sys

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS


reload(sys)
sys.setdefaultencoding('utf-8')



#APPEND_SLASH=False

ACCOUNT_ACTIVATION_DAYS = 7

DEFAULT_FORM_EMAIL = ''
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSOWORD = ''
EMAIL_USE_TLS = False


DEBUG = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (
)

MANAGERS = ADMINS

if 'SERVER_SOFTWARE' in os.environ:
    # SAE 用，根据 SAE  MYSQL数据库配置填写下面参数，一般都是这样的
    import sae.const
    MYSQL_DB = sae.const.MYSQL_DB
    MYSQL_USER = sae.const.MYSQL_USER
    MYSQL_PASS = sae.const.MYSQL_PASS
    MYSQL_HOST_M = sae.const.MYSQL_HOST
    MYSQL_HOST_S = sae.const.MYSQL_HOST_S
    MYSQL_PORT = sae.const.MYSQL_PORT
else:
    # Local 本地调试用，便于导出数据库,根据本地MYSQL数据库填写下面参数
    MYSQL_DB = 'osf'
    MYSQL_USER = 'root'
    MYSQL_PASS = ''
    MYSQL_HOST_M = '127.0.0.1'
    MYSQL_HOST_S = '127.0.0.1'
    MYSQL_PORT = '3306'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': MYSQL_DB,
        'USER': MYSQL_USER,
        'PASSWORD': MYSQL_PASS,
        'HOST': MYSQL_HOST_M,
        'PORT': MYSQL_PORT,
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
#TIME_ZONE = 'America/Chicago'
TIME_ZONE = 'Asia/Shanghai'


# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-cn'
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
print BASE_DIR
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'
MEDIA_PATH = os.path.join(BASE_DIR,'media')
print MEDIA_PATH
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"

# FILEBROWSER
DEFAULT_FILE_STORAGE= 'django.core.files.storage.FileSystemStorage'
FILEBROWSER_DIRECTORY = 'uploads/'
FILEBROWSER_MEDIA_ROOT = MEDIA_ROOT
FILEBROWSER_MEDIA_URL = MEDIA_URL
FILEBROWSER_VERSIONS_BASEDIR = '_versions/'
FILEBROWSER_ADMIN_VERSIONS = ['thumbnail', 'small', 'medium', 'big', 'large']
FILEBROWSER_ADMIN_THUMBNAIL = 'admin_thumbnail'


# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'
STATIC_PATH = os.path.join(BASE_DIR,'static')

# Additional locations of static files
STATICFILES_DIRS = ( 
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
 )
# STATICFILES_DIRS += ( os.path.join( os.path.dirname( "__file__" ), 'static' ) , )
# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = ( 
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
#   'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#   'django.contrib.staticfiles.finders.DefaultStorageFinder',
 )

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'qee8=gi8mq0o=luoch%af7+_93f8rgtnva0vffc$co5es(&amp;rld'

TEMPLATE_CONTEXT_PROCESSORS += ( "django.core.context_processors.request",
 )
TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.static',)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = ( 
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
 )
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
                 TEMPLATE_PATH,
 )
# TEMPLATE_DIRS += ( os.path.join( os.path.dirname( "__file__" ), 'templates' ) , )



MIDDLEWARE_CLASSES = ( 
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
 #   'django.contrib.sites.middleware.CurrentSiteMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
 )

ROOT_URLCONF = 'osf.urls'

# Python dotted path to the WSGI application used by Django's runserver.

WSGI_APPLICATION = 'osf.wsgi.application'


INSTALLED_APPS = ( 
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # comment
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'grappelli',
    'filebrowser',
     'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
     'django.contrib.admindocs',
    'accounts',
    'osf',
    'south',
    # 用户注册功能所需要的应用
    'userena',
    'guardian',
    'easy_thumbnails',
    'restapi',
    'rest_framework',
    'post',
    'spost',
    'album',
    'comment',
    'tag',
    'notification',
    'event',
    'like',
    'follow',
    #'django.contrib.markup',

 )

# userena登录相关设置
USERENA_SIGNIN_REDIRECT_URL = '/'
USERENA_SIGNIN_AFTER_SIGNUP = True
#LOGIN_REDIRECT_URL = '/user/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'
# userena在用户注册后不需要执行激活操作(默认为True)
USERENA_ACTIVATION_REQUIRED = False
USERENA_DISABLE_PROFILE_LIST = False

USERENA_MUGSHOT_SIZE = 140
USERENA_MUGSHOT_GRAVATAR = True
#USERENA_MUGSHOT_PATH = '/mugshots/%(username)s/'
# Django-guardian所需要的设置
ANONYMOUS_USER_ID = -1



# Email后端应用供userena使用。
Email_BACKEND = 'django.core.mail.backends.dummy.Email_Backend'
# 使用UserenaProfile
AUTH_PROFILE_MODULE = 'accounts.MyProfile'
# userena backends settings
AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# memcahce
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 6000,
    }
}

# django rest framework
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    # ]
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGE_SIZE': 10
}


#七牛配置#######################################
qiniu_access_key = ''
qiniu_secret_key = ''
qiniu_bucket_name = ''
qiniu_bucket_domain = ''
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
