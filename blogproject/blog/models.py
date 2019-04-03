from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    # 分类
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    """标签"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Post(models.Model):
    """文章"""
    # 标题
    title = models.CharField(max_length=70)
    # 正文
    body = models.TextField()
    # 创建时间
    created_time = models.DateField()
    # 最后一次修改时间
    modified_time = models.DateField()

    # 文章摘要
    excerpt = models.CharField(max_length=200,blank=True)

    # 分类
    category = models.ForeignKey(Category)
    # 标签
    tags = models.ManyToManyField(Tag,blank=True)

    # 文章作者
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title