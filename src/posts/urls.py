from django.conf.urls import include, url
from django.contrib import admin
from .views import post_list, post_create, post_detail, post_delete, post_update

urlpatterns = [
    # Examples:
    # url(r'^$', 'postool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^(?P<id>\d+)/delete/$', post_delete),
    url(r'^(?P<id>\d+)/edit/$', post_update, name='update'),

]
