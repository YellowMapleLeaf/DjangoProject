from django.db import models

# Create your models here.

#自定义管理器类，重写get_queryset方法，修改原始查询集方法
class myManager(models.Manager):
     def get_queryset(self):
         return super(myManager, self).get_queryset().filter(isDelete=False)
     #定义创建学生数据的方法
     def createData(self,name,sex,age,contend,grade):
         #获取调用类的类名
         # s=self.model()
         # s.sname=name
         # s.sgender=sex
         # s.sage=age
         # s.scontend=contend
         # s.sgrade=grade
         # s.save()
         self.sname = name
         self.sgender = sex
         self.sage = age
         self.scontend = contend
         self.sgrade = grade
         self.save()

class Grades(models.Model):
    gname=models.CharField(max_length=20)
    gdate=models.DateTimeField()
    ggrilnum=models.IntegerField()
    gboynum=models.IntegerField()
    isDelete=models.BooleanField(default=False)
    #定义元信息
    class Meta:
        #定义数据库中的库名
        db_table="grades"
        #定义数据的排序顺序，升序为id，降序为-id
        # ordering=["id"]

class Student(models.Model):
    #创建学生
    @classmethod
    def createStudent(cls,name,sex,age,contend,grade):
        s=cls(sname=name,sgender=sex,sage=age,scontend=contend,sgrade=grade)
        s.save()

    #重新定义管理器，那么object的管理器就不能用了
    manager=myManager()
    sname=models.CharField(max_length=20)
    sgender=models.BooleanField()
    sage=models.IntegerField()
    scontend=models.CharField(max_length=20)
    isDelete=models.BooleanField(default=False)
    sgrade=models.ForeignKey("Grades")
    class Meta:
        db_table="student"
        # ordering=["id"]




