from django.db import models
import uuid
from django.contrib.auth.models import User
from article.models import ArticlePost
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.
class Comment(models.Model): # 博文评论
    article = models.ForeignKey(
        ArticlePost,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = '评论'
        
    def __str__(self):
        return self.body[:20]