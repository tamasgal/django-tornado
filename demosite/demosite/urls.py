from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    (r'^hello-django', 'demosite.views.hello'),
)
