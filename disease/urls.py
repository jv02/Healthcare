from django.conf.urls import url, include

from . import views

app_name = 'disease'

urlpatterns = [

    url(r'^visu/$', views.visu, name='visu'),
]