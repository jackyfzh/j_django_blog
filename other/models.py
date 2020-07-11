from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from model_utils.models import TimeStampedModel
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
        verbose_name_plural = '友链'

    def __str__(self):
        return self.title

class SiteMessage(TimeStampedModel):
    content = models.TextField(verbose_name="正文")

    class Meta:
        verbose_name_plural = '全站公告'

    def __str__(self):
        return self.content[:20]