from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^hello/$',views.hello),
    url(r'^urlRerverse/$',views.urlRerverse,name='rerverse'),
    url(r'^new/$',views.new)
]