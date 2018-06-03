from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^category/(\d+)/$',views.category),
    # 用（\d+）接收前面传过来的参数，然后显示对应的文章
    url(r'^articalShow/(\d+)/$',views.articalShow,name='articalShow'),
    url(r'^userComment/$',views.userComment,name='post_comment'),
    url(r'^getCommentList/$',views.getCommentList,name='getCommentList'),
    url(r'^contribute/$',views.contribute,name='contribute'),


]
