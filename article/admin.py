from django.contrib import admin
from .models import ArticlePost
from .models import ArticleColumn
# Register your models here.
admin.site.register(ArticleColumn)
admin.site.register(ArticlePost)