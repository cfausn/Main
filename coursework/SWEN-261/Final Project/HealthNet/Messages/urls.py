from django.conf.urls import url

from . import views

urlpatterns = {
    url(r'^$', views.messages, name='messages'),
    url(r'create', views.createMessage, name='createMessage'),
}