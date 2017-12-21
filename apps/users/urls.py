from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'main$', views.index),
    url(r'friends$',views.friend),
    url(r'friends/add$',views.friend_add),
    url(r'users/login$',views.login),
    url(r'users/create$',views.create),
    url(r'users/success$',views.success),
    url(r'users/logout$',views.logout),
    url(r'users/(?P<id>\d+)$', views.show),
    url(r'users/(?P<id>\d+)/delete$', views.friend_del),
]