from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

from .models import Blog

def home(request):
    return HttpResponse("im from the blog view home")

def all_blogs(request):
    #blogs_data = Blog.objects.all()
    blogs_data = Blog.objects.order_by('-date')
    return render(request , 'all_blogs.html',{'blogs_data' : blogs_data})

def detail(request,blog_id):
    curr_id = get_object_or_404(Blog,pk=blog_id)
    return render(request , 'detail.html',{'this_id' : curr_id})
