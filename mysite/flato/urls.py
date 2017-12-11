from django.contrib.auth import views as auth_views
from rest_framework import serializers, viewsets, routers
from . import views
from django.conf.urls import include, url




urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logout.html'}, name='logout'),
]
