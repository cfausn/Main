from django.conf.urls import url

from . import views

urlpatterns = {
    url(r'^$', views.index, name='index'),
    url(r'^(?P<theId>\d+)/edit$', views.edit, name='edit'),
    url(r'^editposted$', views.edit, name='editposted'),
    url(r'^(?P<theId>\d+)/password/$', views.password, name='password')
}