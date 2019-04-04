from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Post


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request,'blog/index.html',context={
        'title':'我的博客主页',
        'welcome':'欢迎访问我的博客首页',
        'post_list':post_list
    })
