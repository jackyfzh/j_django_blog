from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.
class Friend(models.Model):
    # 标题
    title = models.CharField(max_length=50, blank=True)
    # 网址
    path = models.CharField(max_length=100, blank=True)
    # 简介
    main = RichTextField(max_length=500, blank=True)
    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return self.title