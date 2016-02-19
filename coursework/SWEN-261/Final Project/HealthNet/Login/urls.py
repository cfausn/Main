from django.conf.urls import url

from . import views

urlpatterns = {
    url(r'^redirect.html$', views.user_redirect),
    url(r'^$', views.user_login, name='login'),
}