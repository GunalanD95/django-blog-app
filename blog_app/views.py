from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView
# Create your views here.



def index(request):
    blog = Blog.objects.all()
    length_of_blogs = len(blog) - 1
    return render(request, 'blog_app/add_blog.html',{'blogs':blog , 'n': range(length_of_blogs)})

class addblog(ListView):
    model = Blog
    context_object_name = 'blogs'

def blog(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    return render(request, 'blog_app/blog.html', 
                  {'blog': blog})