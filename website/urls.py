from django.conf.urls import *
from . import  views

urlpatterns = [

    url(r'^index/$',views.index),
    url(r'^time/$',views.time),
    url(r'^foo/(\d{4})/$',views.foo),
    url(r'^bar/(?P<id>\d{4})/(?P<name>\w+)/$',views.bar)
]
