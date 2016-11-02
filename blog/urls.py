from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.staticfiles.views import serve


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^addlike/(?P<pk>[0-9]+)/$', views.addlike, name ='addlike'),
    url(r'^addcomment/(?P<pk>[0-9]+)/$', views.addcomment, name ='addcomment'),
    url(r'^adddislike/(?P<pk>[0-9]+)/$', views.adddislike, name ='adddislike'),
    url(r'^page/(\d+)/$', views.post_list, name = 'post_list'),
    url(r'^category/get/(?P<category_id>\d+)/$', views.post_cat, name='post_cat'),
    url(r'^keyword/(?P<id>\d+)/$', views.keywords, name='keywords'),
]

# if settings.DEBUG:
#     urlpatterns += [
#         url(r'^media/(?P<path>.*)$', serve,
#             {'document_root': settings.MEDIA_ROOT}),
#         url(r'^static/(?P<path>.*)$', serve,
#             {'document_root': settings.STATIC_ROOT}),
#     ]