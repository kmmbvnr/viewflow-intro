from django.conf.urls import patterns, include, url
from django.contrib import admin
from viewflow import views as viewflow
from .helloworld.flows import HelloWorldFlow


urlpatterns = patterns(
    '',
    url(r'^flows/', include([
        HelloWorldFlow.instance.urls,
        url('^$', viewflow.ProcessListView.as_view(), name='index'),
        url('^tasks/$', viewflow.TaskListView.as_view(), name='tasks'),
        url('^queue/$', viewflow.QueueListView.as_view(), name='queue'),
        url('^details/(?P<process_pk>\d+)/$', viewflow.ProcessDetailView.as_view(), name='details'),
    ], namespace=HelloWorldFlow.instance.namespace), {'flow_cls': HelloWorldFlow}),
    url(r'^admin/', include(admin.site.urls)),
)
