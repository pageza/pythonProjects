from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.log_in),
    url(r'^register$', views.create_user),
    url(r'^books$', views.success),

    url(r'^addReview$', views.),

    url(r'^book/(?P<id>\d+)$', views.),
    url(r'^book/(?P<id>\d+)/add$', views.),
    url(r'^book/(?P<id>\d+)/destroy$', views.),
    url(r'^book/(?P<id>\d+)/update$', views.),

    url(r'^user/(?P<id>\d+)$', views.),
    url(r'^user/(?P<id>\d+)/add$', views.),
    url(r'^user/(?P<id>\d+)/destroy$', views.),
    url(r'^user/(?P<id>\d+)/update$', views.),


]
