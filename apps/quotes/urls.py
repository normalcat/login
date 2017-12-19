from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'quotes$', views.index),
    url(r'quotes/add$', views.add),
    url(r'users/(?P<id>\d+)$$', views.show),
]