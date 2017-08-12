from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.create_user),
    url(r'^success$', views.success),
    url(r'^sessions$', views.log_in),
    url(r'^error$', views.error),
    url(r'^create_secret$', views.create_secret),
    url(r'^popsecret$', views.popsecret),
    url(r'^like/(?P<id>\d+)$', views.like),




]
