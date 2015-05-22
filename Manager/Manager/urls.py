from django.conf.urls import patterns, include, url
from Manager_App.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^Add/', AddContact),
    url(r'^list/', Listing),
    url(r'^delete_name/(?P<pid>[-\w]+)/$', Delete),
                       
)
