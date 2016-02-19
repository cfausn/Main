from django.conf.urls import url

from . import views

urlpatterns = {
    url(r'^$', views.index, name='index'),
    url(r'^(?P<appointment_id>[0000-9999]+)$', views.apppointmentDetails , name = 'appointmentDetails'),
    url(r'^(?P<year>[0000-9999]+)/(?P<month>[00-99]+)/(?P<day>[00-99]+)/(?P<user_id>[00000-99999]+)$',
        views.scheduleDetails, name='schedule'),
    url(r'^(?P<year>[0000-9999]+)/(?P<month>[00-99]+)/(?P<user_id>[00000-99999]+)$',
        views.monthView, name='monthView'),
    url(r'^(?P<year>[0000-9999]+)/(?P<user_id>[00000-99999]+)$',
        views.yearView, name='yearView'),
    url(r'^(?P<appointment_id>[0000-9999]+)/edit$', views.editAppointment , name = 'editAppointment'),
    url(r'^(?P<appointment_id>[0000-9999]+)/delete$', views.deleteAppointment , name = 'deleteAppointment'),
    url(r'^create/', views.createAppointment, name='createAppointment'),
}