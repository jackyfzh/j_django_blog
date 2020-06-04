from django.db import models
import uuid
from mdeditor.fields import MDTextField
# 导入内建的User模型。
from django.contrib.auth.models import User
# timezone 用于处理时间相关事务。
from django.utils import timezone
from taggit.managers import TaggableManager
from PIL import Image
from django.urls import reverse
# Create your models here.
class ArticleColumn(models.Model):
    """
    栏目的 Model
    """
    # 栏目标题
    title = models.CharField(max_length=100, blank=True)
    # 创建时间
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 作者
    # 文章栏目的 “一对多” 外键
    column = models.ForeignKey(
        ArticleColumn,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='article'
    )
    tags = TaggableManager(blank=True)
    belongs = models.CharField(max_length=58,blank=True)
    total_views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=75) # 标题
    avatar = models.ImageField(upload_to='article/%Y%m%d/', blank=True) # 标题图
    # 保存时处理图片
    def save(self, *args, **kwargs):
        # 调用原有的 save() 的功能
        article = super(ArticlePost, self).save(*args, **kwargs)

        # 固定宽度缩放图片大小
        if self.avatar and not kwargs.get('update_fields'):
            image = Image.open(self.avatar)
            (x, y) = image.size
            new_x = 400
            new_y = int(new_x * (y / x))
            resized_image = image.resize((new_x, new_y), Image.ANTIALIAS)
            resized_image.save(self.avatar.path)

        return article
    main = models.CharField(max_length=100) # 简介
    body = MDTextField() # 正文
    created = models.DateTimeField(default=timezone.now) # 创建时间
    updated = models.DateTimeField(auto_now=True) # 修改时间

    class Meta:
        ordering = ("-created",) # 文章排序方式
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])

    def was_created_recently(self):
        diff = timezone.now() - self.created

        # if diff.days <= 0 and diff.seconds < 60:
        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            return True
        else:
            return False