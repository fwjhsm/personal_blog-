from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'blog/index.html',context={
        'title':'我的博客主页',
        'welcome':'欢迎访问我的博客首页'
    })
