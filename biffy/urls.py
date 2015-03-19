from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'biffy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', include('floweditor.urls')),
	url(r'^floweditor/', include('floweditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
