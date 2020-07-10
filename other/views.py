from django.shortcuts import render
from .models import Friend
# Create your views here.
def about(request):
    return render(request, "other/about.html")

def friends(request):
    friends = Friend.objects.all()
    contaxt = {"friends" : friends}
    return render(request, "other/friend.html",contaxt)

def blog_comment(request):
    return render(request, "other/comment.html")