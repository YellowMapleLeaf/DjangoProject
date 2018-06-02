from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json
def HomePage(request):
    # contents=[
    #     {
    #         'title': '物流的纯css实现方法',
    #         'img': 'static/myWebApp/img/head.png',
    #         'text': '　　首先我们来看看UI给出的设计图。 为什么到达是最前面，为什么物流顺序是倒叙的，这是什么用户习惯，这是我拿到设计稿的问题，但是这里不谈设计，因为审美这个东西无法评估。那么这里我就做一个顺序的来对比一下吧。 由于建采这个项目比较赶，我基本只拿到一直png设计稿和一些psd文件，所以这里我们不考虑用图片和 ...',
    #         'username': '博客园',
    #         'time': '2018-05-10 18:10',
    #     },
    #     {
    #         'title': '物流的纯css实现方法',
    #         'img': 'static/myWebApp/img/head.png',
    #         'text': '　　首先我们来看看UI给出的设计图。 为什么到达是最前面，为什么物流顺序是倒叙的，这是什么用户习惯，这是我拿到设计稿的问题，但是这里不谈设计，因为审美这个东西无法评估。那么这里我就做一个顺序的来对比一下吧。 由于建采这个项目比较赶，我基本只拿到一直png设计稿和一些psd文件，所以这里我们不考虑用图片和 ...',
    #         'username': '博客园',
    #         'time': '2018-05-10 18:10',
    #     }
    # ]
    # return render(request, 'myWebApp/HomePage.html', {"contentList": contents})
    with open(r'H:\Djangoproject\myWebProject\static\myWebApp\db\content.json','r',encoding="utf-8") as file:
        contents=file.read()
        JsonContents=json.loads(contents)
        pageNum=len(JsonContents)
        pageNumList=range(1,pageNum+1)
        print(pageNumList)
        return render(request,'myWebApp/HomePage.html',{"contentList":JsonContents,"pageNum":pageNumList})



