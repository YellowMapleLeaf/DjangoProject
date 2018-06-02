from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("欢迎来到index")

def hello(request):
    return render(request,'myApp/hello.html')
def urlRerverse(request):
    return render(request,"myApp/urlRerverse.html")

def new(request):
    return render(request,'myApp/new.html')