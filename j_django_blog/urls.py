"""j_django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import notifications.urls

admin.site.site_title = '博客网站后台'
admin.site.site_header = 'Jacky的个人网站后台'

urlpatterns = [
    path('jackypy/blog/background/ng', admin.site.urls),
    path('', include('article.urls', namespace='article')),
    path('userprofile/', include('userprofile.urls', namespace='userprofile')),
    path('comment/', include('comment.urls', namespace='comment')),
    path('other/', include('other.urls', namespace='other')),
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    path('notice/', include('notice.urls', namespace='notice')),
    path('mdeditor/', include('mdeditor.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
