from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
app_name = 'home'

urlpatterns = [
    url(r'^$', views.homepage,name='home'),
    url(r'^detail/(?P<id>[\w-]+)/$', views.detail, name='detail'),
]

urlpatterns += staticfiles_urlpatterns()