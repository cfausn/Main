"""HealthNet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from . import views



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.indexView, name='indexView' ),
    url(r'^HealthNet/', include('HealthNet.urls', namespace="HealthNet")),
    url(r'^Register/', include('Register.urls', namespace="Register")),
	url(r'^Messages/', include('Messages.urls', namespace="Messages")),
	url(r'^Schedule/', include('Schedule.urls', namespace="Schedule")),
	url(r'^Profiles/', include('Profiles.urls', namespace="Profiles")),
    url(r'^Login/', include('Login.urls', namespace="Login")),
    url(r'^notifications/', include('notifications.urls', namespace="notifications")),
]

handler404 = 'HealthNet.views.custom404Page'

