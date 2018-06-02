from django.shortcuts import render
from django.http import HttpResponse
from .models import Friends
# Create your views here.
def index(request):
    return HttpResponse("index")

def showFriends(request):
    friendList=Friends.objects.all()
    return render(request,"myApp/friends.html",{"friends":friendList})

def submitimg(request):
    return render(request,"myApp/img.html")

import os
from django.conf import settings
def savefile(request):
    if request.method=="POST":
        f=request.FILES["img"]
        filePath=os.path.join(settings.BASE_DIR,"static/upfile",f.name)
        with open(filePath,"wb") as file:
            for data in f.chunks():
                file.write(data)
        return HttpResponse("上传成功")
    else:
        return HttpResponse("上传失败")

from django.core.paginator import Paginator
def friendpage(request,pageNum):
    all=Friends.objects.all()
    pag=Paginator(all,3)
    page=pag.page(pageNum)

    # allFriends=Friends.objects.all()
    # # 每四条数据一个页
    # paginator=Paginator(allFriends,4)
    # page=paginator.page(pageNum)

    return render(request,"myApp/friendpage.html",{"friends":page})


def ajaxfriends(request):
    return render(request, "myApp/ajaxfriends.html")

from django.http import JsonResponse
def friendsinfo(request):
    fList=Friends.objects.all()
    li=[]
    for i in fList:
        li.append([i.fName,i.fSingle])
    return JsonResponse({"data":li})

def fulltext(request):
    return render(request, "myApp/fulltext.html")


def getFullText(request):
    st=request.GET.get("str")
    return HttpResponse(st)