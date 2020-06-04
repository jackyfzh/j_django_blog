from django.urls import path
from . import views
# 正在部署的应用的名称
app_name = 'other'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('friends/', views.friends, name='friends'),
]