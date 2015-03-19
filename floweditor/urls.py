from django.conf.urls import patterns, url

from floweditor import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^getScenarios/$', views.getScenarios, name='getScenarios'),
    url(r'^getScenarioFiles/$', views.getScenarioFiles, name='getScenarioFiles'),
    url(r'^getFlowFiles/$', views.getFlowFiles, name='getFlowFiles'),
    url(r'^getFlowFileContent/$', views.getFlowFileContent, name='getFlowFileContent'),

)