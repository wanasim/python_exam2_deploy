from django.conf.urls import url
from . import views

app_name="beltapp"

urlpatterns=[
    url(r'^join/(?P<id>\d+)$', views.join, name='join'),
    # url(r'^remove/(?P<id>\d+)$', views.removeItem, name='remove'),
    url(r'^travel/(?P<id>\d+)$', views.travelInfo, name="travelInfo"),
    # url(r'^deleteItem/(?P<id>\d+)$', views.deleteItem, name="delete"),
    url(r'^travel_plan/create$', views.createTravel, name='createTravel'),
    url(r'^travel_plan/add$', views.addTravel, name='addTravel'),
    url(r'^$', views.index, name="index")
]
