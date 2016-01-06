# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [   
    url(r'^$', views.index, name='index'),
    url(r'^servers', views.servers, name='servers'),
    url(r'^register', views.register, name='register'),
]