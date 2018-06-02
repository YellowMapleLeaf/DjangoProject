from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^(\d+)$',views.info),
    url(r'^grades/$',views.grade),
    url(r'^students/$',views.student),
    url(r'^grades/(\d+)',views.gradeStudent),
    url(r'^find/$',views.findStundet),
    url(r'^grilbigger/$',views.grilBigger),
    url(r'^qobjct/$',views.Qobjct),
    url(r'^redirectText',views.redirectText),
    url(r'^main/$',views.main),
    url(r'^login/$',views.login),
    url(r'^deallogin/$',views.dealLogin),
    url(r'inheritBase/$',views.inheritBase,name="bases")
]





