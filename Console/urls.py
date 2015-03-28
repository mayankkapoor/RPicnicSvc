from django.conf.urls import patterns, url

from Console import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
