from django.conf.urls import patterns,url, include
from rest_framework import routers
from restapi import views
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'group', views.GroupViewSet)
router.register(r'album', views.AlbumViewSet)
router.register(r'photo', views.PhotoViewSet)
router.register(r'comment', views.CommentViewSet)
router.register(r'post', views.PostViewSet)
router.register(r'tag', views.TagViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = patterns('',

    # url(r'^album/$', views.AlbumList.as_view()),
    # url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumDetail.as_view()),
    # url(r'^photo/$', views.PhotoList.as_view()),
    # url(r'^photo/(?P<pk>[0-9]+)/$', views.PhotoDetail.as_view()),
    # url(r'^comment/$', views.CommentList.as_view()),
    # url(r'^comment/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view()),
    # url(r'^post/$', views.PostList.as_view()),
    # url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
    # url(r'^tag/$', views.TagList.as_view()),
    # url(r'^tag/(?P<pk>[0-9]+)/$', views.TagDetail.as_view()),
)

urlpatterns += [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

#urlpatterns = format_suffix_patterns(urlpatterns)