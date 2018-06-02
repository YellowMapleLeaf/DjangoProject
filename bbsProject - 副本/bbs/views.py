from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from bbs import models
from django.contrib.auth import login,logout,authenticate

# from .templatetags import custom


#某些模块需要登录之后才能进行操作
from django.contrib.auth.decorators import login_required
# Create your views here.

# 模块列表
category_list = models.Category.objects.filter(set_as_top_menu=True).order_by('position_index')

####################################################
#  name         :index
#  function     :重定向到首页
#  parameters_in:
#            request:客户端的信息
#  parameters_out:
#           category/1/：首页URL
####################################################
def index(request):
    # return render(request,'bbs/index.html',{"category_list":category_list})
    return HttpResponseRedirect("category/1/")


####################################################
#  name         :category
#  function     :动态显示模块
#  parameters_in:
#            request:客户端的信息
#            id     :模块的ID号
#  parameters_out:
#           bbs/index.html：返回index.html网页
#           category_list：模块列表
#           category_object：对应的模块
#           article_list：模块的文章列表
####################################################
def category(request,id):
    #获取相对于id名的category对象
    category_object=models.Category.objects.get(id=id)
    # 获取模块的文章
    if category_object.id==1:
        article_list = models.Article.objects.filter(status='published')
    else:
        article_list = models.Article.objects.filter(category_id=category_object.id, status='published')
    return render(request,'bbs/index.html',{"category_list":category_list,
                                            "category_object":category_object,
                                            "article_list":article_list})

####################################################
#  name         :bbs_login
#  function     :用户登录，验证
#  parameters_in:
#            request:客户端的信息
#  parameters_out:
#           request.GET.get('next','/bbs')：返回上一个页面
#           newlogin.html：登录的页面
#           login_err：密码输入的错误时的错误信息
####################################################
def bbs_login(request):
    if request.method == 'POST':
        print(request.POST)
        #验证用户
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user is not None:
            #登录
            login(request,user)
            return HttpResponseRedirect(request.GET.get('next','/bbs'))
        else:
            login_err = "帅哥，美女，你的用户名或者密码是不是写错了，没有登录进入"
            return render(request,'newlogin.html',{'login_err':login_err})

    return render(request,'newlogin.html')

####################################################
#  name         :bbs_logout
#  function     :注销用户
#  parameters_in:
#            request:客户端的信息
#  parameters_out:
#           request.GET.get('next', '/bbs')：重定向到上一个网页
#
####################################################
def bbs_logout(request):
    logout(request)
    return HttpResponseRedirect(request.GET.get('next', '/bbs'))

####################################################
#  name         :newlogin
#  function     :登录
#  parameters_in:
#            request:客户端的信息
#  parameters_out:
#
#
####################################################
# def newlogin(request):
#     return render(request,'newlogin.html')



####################################################
#  name         :userComment
#  function     :提交用户评论
#  parameters_in:
#            request:客户端的信息
#  parameters_out:
#
#
####################################################
def userComment(request):
    # return HttpResponse("isok?")
    if request.method == 'POST':
        comment=models.Comment(comment_type=request.POST.get("comment_type"),
                               comment=request.POST.get("comment"),
                               article_id=request.POST.get("article_id"),
                               parent_comment_id=request.POST.get("parent_comment_id",None),
                               user_id=request.user.userprofile.id
                               )
        comment.save()
        return HttpResponse('post-comment-success')


####################################################
#  name         :articalShow
#  function     :文章的显示
#  parameters_in:
#            request:客户端的信息
#            artical_id:文章的ID
#  parameters_out:
#           category_list：模块的列表
#           artical_info：文章的相关信息
#           img_position：文章左侧支付宝等图标
#           bbs/article-show.html：显示文章的网页
####################################################
def articalShow(request,artical_id):
    # 规定左侧图标的位置
    img_position=[{"x":10,"y":-259},
                  {"x": -50, "y": -259},
                  {"x": -238, "y": -531},
                  {"x": -121, "y": -259},
                  {"x": -178, "y": -246},
                  {"x": -249, "y": -245},
                  {"x": -350, "y": -260},
                  ]
    # 获取文章的信息
    artical_info = models.Article.objects.get(id=artical_id)
    return render(request, 'bbs/article-show.html', {"category_list": category_list,
                                                     "artical_info":artical_info,
                                                     "img_position":img_position})
####################################################
#  name         :getCommentList
#  function     :获取文章的评论列表
#  parameters_in:
#            request:客户端的信息
#            artical_id:文章的ID
#  parameters_out:
#           comment_html：文章列表的html格式
####################################################
def getCommentList(request):
    artical_id=request.GET.get("artical_info.id")
    # 获取文章的信息
    artical_info = models.Article.objects.get(id=artical_id)
    # 获取对应文章的所有评论
    comments_list = artical_info.comment_set.select_related()
    comment_tree = treeStructure(comments_list)
    comment_html = commentHTML(comment_tree)
    return HttpResponse(comment_html)

####################################################
#  name         :treeNode
#  function     :构造树的节点
#  parameters_in:
#               comment_dict:构造树结构用的字典
#               comment：每一条评论
#  parameters_out:
#               comment_dict：构造完成之后的字典
#
####################################################

def treeNode(comment_dict,comment):
    #如果没有上级评论，那么这是顶级评论
    global leakage_comment_set
    if comment.parent_comment is None:
        comment_dict[comment]={}
        return
    else:
        #如果不是顶级评论，那么循环字典，看当前评论的父级评论在哪一个地方
        for k,v in comment_dict.items():
            #如果找到某条评论的父级评论
            if comment.parent_comment==k:
                comment_dict[comment.parent_comment][comment]={}
                return
            #如果没有找到，那么就继续往下找
            else:
                treeNode(v,comment)




####################################################
#  name         :treeStructure
#  function     :构造树结构
#  parameters_in:
#            comments_list:该文章的所有评论
#  parameters_out:
#            comment_dict：构造完成后的树
#
####################################################
def treeStructure(comments_list):
    comment_dict = {}
    # print(comments_list)
    for comment in comments_list:
        # print(dir(comment))
        treeNode(comment_dict,comment)

    # print('----------------')
    # for k, v in comment_dict.items():
    #     print(k, v)
    return comment_dict


def truncate_url(img_obj):
    return  img_obj.name.split("/",maxsplit=1)[-1]



####################################################
#  name         : commentHTML
#  function     :构造comment的HTML标签
#  parameters_in:
#               comment_tree:构造好树结构的评论
#  parameters_out:
#               html:html标签字符串
#
####################################################
def commentHTML(comment_tree):
    html=""
    #构造顶级评论的标签
    for k,v in comment_tree.items():
        #图片地址转换
        img_path=truncate_url(k.user.head_img)
        temp="<div class='root-comment comment-style'>" \
             "<span><a href='#'><img src='/static/%s '></a></span>" %img_path\
             + "<span class='author'>%s</span>"%k.user.name\
             +"<span class='time'>%s</span>"%k.date \
             + "<span class='glyphicon glyphicon-thumbs-up' aria-hidden='true'></span>" \
             +"<span class='thumb-num'>num</span>" \
             + "<span class='glyphicon glyphicon-triangle-bottom' target='%s' aria-hidden='true'></span>"% k.id \
             + "<div class='report hide'id='%s'>举报</div>" %k.id \
             +"<div class='content'>%s</div>"%k.comment \
             + "<div><span class='reply' target='%s'>回复</span></div>" %k.id \
             +"</div><hr>"
        html+=temp
        html+=nodeHTML(v,10)
    return html


####################################################
#  name         : nodeHTML
#  function     :递归构造顶级评论下的每一个评论的HTML标签
#  parameters_in:
#               comment_tree:构造好树结构的评论
#  parameters_out:
#               html:html标签字符串
#
####################################################
# "<span><img src='/static/{{%s | truncate_url}}'></span>"%k.comment.article.head_img
def nodeHTML(comment_tree,margin_left):
    html=""
    for k,v in comment_tree.items():
        # 图片地址转换
        img_path = truncate_url(k.user.head_img)
        temp= "<div class='comment-node comment-style' style='margin-left:%spx;'>"%margin_left\
              +"<span><a href='#'><img src='/static/%s '></a></span>" %img_path\
              +"<span class='author'>%s</span>"%k.user.name\
              +"<span class='time'>%s</span>"%k.date\
              +"<span class='glyphicon glyphicon-thumbs-up' aria-hidden='true'></span>" \
              +"<span class='thumb-num'>num</span>" \
              +"<span class='glyphicon glyphicon-triangle-bottom' target='%s' aria-hidden='true'></span>" %k.id\
              +"<div class='report hide' id='%s'>举报</div>" %k.id\
              +"<div class='content'>%s</div>"%k.comment \
              + "<div><span class='reply' target='%s'>回复</span></div>" %k.id\
              +"</div><hr>"

        html+=temp
        html+=nodeHTML(v,margin_left+20)
    return html

####################################################
#  name         : contribute
#  function     : 投稿
#  parameters_in:
#               request:客户端发来的信息
#  parameters_out:
#
#
####################################################
def contribute(request):
    pass