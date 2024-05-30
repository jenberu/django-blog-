from django.shortcuts import render,get_list_or_404
from .models import Post
from django.http import Http404
def post_list(request):
    posts=Post.objects.all()
    return render(request,'list.html',{'posts':posts})
def post_detail(request,id):
    try:
        post=get_list_or_404(id=id)
    except Post.DoesNotExist:
        raise Http404("No Post found")
    return render(request,'detail.html',{'post':post})
    
    
       



# Create your views here.
