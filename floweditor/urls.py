from django.conf.urls import patterns, url

from floweditor import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^getScenarios/$', views.getScenarios, name='getScenarios'),
    url(r'^getScenarioFlows/$', views.getScenarioFlows, name='getScenarioFlows'),
    url(r'^getFlowFiles/$', views.getFlowFiles, name='getFlowFiles'),
    url(r'^getFlowFileContent/$', views.getFlowFileContent, name='getFlowFileContent'),
    url(r'^saveFlowFileContent/$', views.saveFlowFileContent, name='saveFlowFileContent'),
    url(r'^downloadScenarioZip/$', views.downloadScenarioZip, name='downloadScenarioZip'),
    url(r'^formatXML/$', views.formatXML, name='formatXML')

)