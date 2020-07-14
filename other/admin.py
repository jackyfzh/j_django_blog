from django.contrib import admin
from .models import Friend, SiteMessage, Timeline
# Register your models here.
admin.site.register(Friend)
admin.site.register(SiteMessage)
admin.site.register(Timeline)