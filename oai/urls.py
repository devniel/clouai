#!--coding:utf-8--#

from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

admin.autodiscover()

import views

urlpatterns = patterns('',
	url(r'^$', 
		views.index, 
		name='index'),
)