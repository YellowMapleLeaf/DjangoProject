from django.db import models
from django.contrib.auth.models import User
import datetime
#出现红色的错误
from django.core.exceptions import ValidationError

# Create your models here.
#帖子
class Article(models.Model):
    #标题
    title=models.CharField(max_length=255)
    #简介
    brief=models.CharField(null=True,blank=True,max_length=255)
    #分类,注意要加引号，因为程序是从上往下执行的
    category=models.ForeignKey("Category")
    #内容
    content=models.TextField(u"文章内容")
    #作者
    author=models.ForeignKey("UserProfile")
    #时间
    pub_date=models.DateTimeField(null=True,blank=True)
    #最后一次修改
    last_modify=models.DateTimeField(auto_now=True)
    #优先级，用来置顶
    priority=models.IntegerField(u'优先级',default=1000)
    #文章标题图片
    head_img = models.ImageField(u'文章标题图片',upload_to='upload')
    #文章状态
    status_chioces=(('draft',u'草稿'),
                    ('published',u'已发布'),
                    ('hidden', u'隐藏'))
    status=models.CharField(choices=status_chioces,default='published',max_length=100)

    def __str__(self):
        return self.title


    ####################################################
    #  name         :clean
    #  function     :用来自定义模型验证，不需要在代码那边控制
    #  parameters_in:
    #
    #  parameters_out:
    #
    #
    ####################################################
    def clean(self):
        # Don't allow draft entries to have a pub_date.
        if self.status == 'draft' and self.pub_date is not None:
            raise ValidationError(('Draft entries may not have a publication date.'))
        # Set the pub_date for published items if it hasn't been set already.
        if self.status == 'published' and self.pub_date is None:
            self.pub_date = datetime.date.today()


#评论
class Comment(models.Model):
    # 评论所属文章，verbose_name为字段起一个别名，用来在admin中显示
    article=models.ForeignKey(Article,verbose_name=u"所属文章")
    #父级评论,通过related_name知道有多少的孩子
    parent_comment=models.ForeignKey('self',related_name="my_children",blank=True,null=True)
    #第一个参数是值，将被存储到数据库里。第二个值是在admim下拉列表的显示
    comment_chioces= ((1,u'评论'),
                      (2,u'点赞'))
    #类型,评论或者点赞
    comment_type=models.IntegerField(choices=comment_chioces,default=1)
    #评论者
    user=models.ForeignKey("UserProfile")
    #评论内容
    comment=models.TextField(blank=True,null=True)
    #评论时间
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s"%(self.comment)
    def clean(self):
        if self.comment_type == 1 and len(self.comment) == 0:
            raise ValidationError(u"评论内容不能为空")

# 板块
class Category(models.Model):
    #板块名
    name=models.CharField(max_length=64,unique=True)
    #简介
    brief=models.CharField(null=True,blank=True,max_length=255)
    #标志位
    set_as_top_menu=models.BooleanField(default=False)
    #展示位置
    position_index=models.SmallIntegerField()
    #版主
    admins=models.ManyToManyField("UserProfile",blank=True)

    def __str__(self):
        return self.name
#用户
class UserProfile(models.Model):
    #关联django中的User
    user=models.OneToOneField(User)
    #昵称
    name=models.CharField(max_length=32)
    #个人简介
    signatrue=models.CharField(max_length=255,blank=True,null=True)
    #头像
    # head_img=models.ImageField(height_field=150,width_field=150,blank=True,null=True)
    head_img = models.ImageField(u'用户图片', upload_to='upload',blank=True, null=True)



    def __str__(self):
        return self.name