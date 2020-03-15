from django.conf.urls import url, include

from . import views

app_name = 'account'

urlpatterns = [

    url(r'^signup/pat/$', views.signup_p, name='signup_p'),
    url(r'^signup_pat/$', views.signup_pat, name='signup_pat'),
    url(r'^login_pat/$', views.login_pat, name='login_pat'),
    url(r'^login/pat/$', views.login_p, name='login_p'),

    url(r'^signup/doc/$', views.signup_d, name='signup_d'),
    url(r'^signup_doc/$', views.signup_doc, name='signup_doc'),
    url(r'^login/doc/$', views.login_d, name='login_d'),
    url(r'^login_doc/$', views.login_doc, name='login_doc'),

    url(r'^logout_doc/$', views.logout_doc, name='logout_doc'),
    url(r'^pat_details/$', views.pat_deatil, name='pat_details'),
    url(r'^record/$', views.record, name='record'),
    url(r'^record_process/$', views.record_process, name='record_process'),
    url(r'^show_patdetails/$',views.show_patdetail,name='show_patdetails'),
]

