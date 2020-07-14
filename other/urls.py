from django.urls import path
from . import views
# 正在部署的应用的名称
app_name = 'other'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('friends/', views.friends, name='friends'),
    path('comment/', views.blog_comment, name='comment'),
    path('timeline/', views.timeline, name='timeline'),
]