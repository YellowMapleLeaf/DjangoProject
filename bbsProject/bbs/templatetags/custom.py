# 自定义过滤器

from django import template
# from django.utils.html import format_html
# 注册我们自定义的标签和过滤器必须在django中
# 自定义过滤器只是一个接受一个或两个参数的python函数
register = template.Library()


####################################################
#  name         :truncate_url
#  function     :截断URL，让图片正常显示
#  parameters_in:
#            img_obj:图片的路径
#  parameters_out:
#           img_obj.name.split("/",maxsplit=1)[-1]：截断后的图片路径
####################################################
@register.filter
def truncate_url(img_obj):
    return  img_obj.name.split("/",maxsplit=1)[-1]


####################################################
#  name         :filter_comment
#  function     : 获取文章的点赞数和评论数
#  parameters_in:
#            article_obj:文章对象
#  parameters_out:
#           comments：
#               comment_count：评论的次数
#               thumb_count：点赞的次数
####################################################
@register.simple_tag
def filter_comment(article_obj):
    # select_related()是django QuerySet的API，它的作用是可以减少SQL query的次数。
    query_set = article_obj.comment_set.select_related()
    comments = {
        'comment_count': query_set.filter(comment_type=1).count(),
        'thumb_count': query_set.filter(comment_type=2).count(),
    }
    return comments

####################################################
#  name         : filter_article_num
#  function     : 获取用户的文章数
#  parameters_in:
#            article_author:文章作者
#  parameters_out:
#
####################################################
@register.simple_tag
def filter_article_num(article_author):
    query_set=article_author.article_set.select_related()
    num=query_set.filter(status='published').count()
    print(num)
    return num
