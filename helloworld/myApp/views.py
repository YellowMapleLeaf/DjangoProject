from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F,Q,Max
from .models import Grades,Student
# Create your views here.

def index(request):
    return HttpResponse("index")

def info(request,num):
    re=HttpResponse()
    re.content="回复你了"
    re.set_cookie("ni","nili")
    return re

from django.shortcuts import  HttpResponseRedirect,redirect
def redirectText(request):
    # return HttpResponseRedirect("/grades")
    return redirect("/grades")


def grade(request):
    print(request.GET.get('a'))
    g=Grades.objects.all()
    return render(request,'myApp/grades.html',{"grades":g})

def student(request):
    s=Student.manager.all()[0:3]
    print(request.path)
    print("************")
    print(request.method)
    print("************")
    print(request.COOKIES)
    print("************")
    print(request.encoding)
    print("************")
    print(request.FILES)
    print("************")
    print(request.GET)
    print("************")
    print(request.session)
    return render(request,'myApp/student.html',{"students":s,"num":10,"str":"hahahahahah"})

def gradeStudent(request,num):

    g=Grades.objects.get(pk=num)
    sList=g.student_set.all()
    return  render(request,'myApp/student.html',{"students":sList})

def findStundet(request):
    s=Student.manager.filter(sname__contains="小")
    return render(request, 'myApp/student.html', {"students": s})

#F对象是为了让一个模型类里面的属性间进行比较
def grilBigger(request):
    grilGrades=Grades.objects.filter(ggrilnum__gt=F("gboynum"))
    return render(request,'myApp/grades.html',{"grades":grilGrades})

#Q对象是实现过滤器的或条件
def Qobjct(request):
    sList=Student.manager.filter(Q(sage__gt=20)|Q(id__gt=3))
    return render(request,'myApp/student.html',{"students":sList})


def main(request):
    username=request.session.get("name","游客")

    return render(request,"myApp/main.html",{"username":username})

def login(request):
    return render(request,"myApp/login.html")


def dealLogin(request):
    username=request.POST.get("username")
    request.session["name"]=username
    request.session.set_expiry(10)
    return redirect("/main/")

def inheritBase(request):
    return render(request,"myApp/inheritBase.html")


