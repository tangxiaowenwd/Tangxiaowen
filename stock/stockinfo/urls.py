#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Time    : 2021/1/23 21:13
# Author  : TangXiaowen
from django.conf.urls import include
from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'login/', views.login),
    url(r'register/', views.register),
    url(r'logout/', views.logout),
    url(r'captcha', include('captcha.urls')),
    url('', views.index),
]
