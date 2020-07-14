from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from model_utils.models import TimeStampedModel
# Create your models here.
class Friend(models.Model):
    # 标题
    title = models.CharField(max_length=50)
    # 网址
    path = models.CharField(max_length=100)
    # 简介
    main = RichTextField(max_length=500)
    # 创建时间
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = '友链'

    def __str__(self):
        return self.title

class SiteMessage(models.Model):
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = '全站公告'

    def __str__(self):
        return self.content[:20]

class Timeline(models.Model):
    author = models.CharField(max_length=10000, blank=True, default="Jacky")
    content = models.TextField()
    path = models.CharField(max_length=10000, blank=True)
    created = models.DateField(default=timezone.now)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = '网站归档'

    def __str__(self):
        return self.content[:20]