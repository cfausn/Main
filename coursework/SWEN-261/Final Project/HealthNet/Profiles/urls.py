from django.conf.urls import url

from . import views

urlpatterns = {
    url(r'^$', views.index, name='index'),
    url(r'^(?P<theId>\d+)/profile$', views.profile, name='details'),
    url(r'^(?P<theId>\d+)/log', views.log, name='log'),
    url(r'^(?P<theId>\d+)/mypatients', views.mypatients, name='mypatients'),
    url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^(?P<theId>\d+)/createPrescription', views.createPrescription, name='createPrescription'),
    url(r'^(?P<theId>\d+)/createSurgery', views.createSurgery, name='createSurgery'),
    url(r'^(?P<theId>\d+)/createTestResults', views.createTestResults, name='createTestResults'),
    url(r'^(?P<theId>\d+)/approveTestResults', views.approveTestResults, name='approveTestResults'),
    url(r'^(?P<theId>\d+)/editMedicalInfo$', views.editMedicalInfo, name='editMedicalInfo'),
    url(r'^statistics', views.statistics, name='statistics'),

    url(r'^chooseMyDoctor', views.chooseMyDoctor, name='chooseMyDoctor'),
    url(r'^inactiveAccounts', views.inactiveUsers, name='inactiveAccounts'),
    url(r'^inputCSV', views.inputCSV, name='inputCSV'),
    url(r'^(?P<theId>\d+)/export', views.export, name='export'),
}