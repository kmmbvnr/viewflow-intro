from django.conf.urls import patterns, include, url
from django.contrib import admin
from viewflow.site import viewsite

urlpatterns = patterns(
    '',
    url(r'^flows/', include(viewsite.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
