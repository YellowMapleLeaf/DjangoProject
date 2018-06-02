from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^friends/$',views.showFriends),
    url(r'^submitimg/$',views.submitimg),
    url(r'^savefile/$',views.savefile),
    url(r'^friendpage/(\d+)/$',views.friendpage),
    url(r'^ajaxfriends/$',views.ajaxfriends),
    url(r'^friendsinfo/$',views.friendsinfo),
    url(r'^fulltext/$',views.fulltext),
    url(r'^getFullText/$',views.getFullText)
]