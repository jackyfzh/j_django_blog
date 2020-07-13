from django.shortcuts import render
from .models import Friend, SiteMessage
# Create your views here.
def about(request):
    return render(request, "other/about.html")

def friends(request):
    friends = Friend.objects.all()
    contaxt = {"friends" : friends}
    return render(request, "other/friend.html",contaxt)

def blog_comment(request):
    return render(request, "other/comment.html")

def messages(request):
    messages = Friend.objects.last()
    contaxt = {"ms" : messages}
    return render(request, "article/list.html",contaxt)