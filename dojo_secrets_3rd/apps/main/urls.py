from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.create_user),
    url(r'^success$', views.success),
    url(r'^sessions$', views.log_in),
    url(r'^create_secret$', views.create_secret),
    url(r'^popsecret$', views.popsecret),
    url(r'^log_out$', views.log_out),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^like/(?P<id>\d+)$', views.like),




]
