from django.contrib import admin
from .models import Grades,Student
# Register your models here.

#
# admin.site.register(Grades)
# admin.site.register(Student)

class studentInfo(admin.TabularInline):
    model = Student
    extra = 2

class studentInfo2(admin.StackedInline):
    model = Student
    extra = 2

@admin.register(Grades)
class gradesAdmin(admin.ModelAdmin):
    #在班级的添加删除页里可以添加关联的学生信息
    inlines = [studentInfo2]

    #自定义显示字段
    list_display = ["gname","gdate","ggrilnum","gboynum","isDelete"]
    #一页5条
    list_per_page = 5
    list_filter = ["gname"]
    search_fields = ["gname"]
    actions_on_bottom = True
    actions_on_top = False

    # 属性先后顺序
    # fields = ["ggrilnum","gboynum","isDelete","gname","gdate"]

    #分组
    fieldsets = [
        ("数量",{"fields":["ggrilnum","gboynum"]}),
        ("基本信息",{"fields":["gname","gdate","isDelete"]}),
    ]

@admin.register(Student)
class studentAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"

    list_display = ["sname", gender, "sage", "scontend", "isDelete"]




# admin.site.register(Grades,gradesAdmin)
# admin.site.register(Student,studentAdmin)

