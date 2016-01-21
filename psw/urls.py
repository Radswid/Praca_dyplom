# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [   
    url(r'^$', views.index, name='index'),
    url(r'^servers', views.servers, name='servers'),
    url(r'^register', views.register, name='register'),
    url(r'^listservers', views.listservers, name='listservers'),
    url(r'^login', auth_views.login, {'template_name':'psw/login.html'}, name='login'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^userview', views.userview, name='userview'),
]
