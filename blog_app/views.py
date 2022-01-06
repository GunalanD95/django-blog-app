from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView, CreateView , UpdateView, DeleteView
from .forms import BlogForm
# Create your views here.



def index(request):
    blog = Blog.objects.all()
    length_of_blogs = len(blog) - 1
    return render(request, 'blog_app/add_blog.html',{'blogs':blog , 'n': range(1,length_of_blogs)})

class AddBlogView(CreateView):
    model = Blog
    template_name = 'blog_app/create_blog.html'
    fields = '__all__'

class UpdateBlogView(UpdateView):
    model = Blog
    template_name = 'blog_app/update_post.html'
    fields = '__all__'

class DeleteBlogView(DeleteView):
    model = Blog
    template_name = 'blog_app/delete_blog.html'
    success_url = '/'

def blog(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    return render(request, 'blog_app/blog.html', 
                  {'blog': blog})

# def create_blog(request):   
#     form = AddBlogView(request.POST)
#     if form.is_valid():
#         print(form.cleaned_data)
#         title = form.cleaned_data['title']
#         content = form.cleaned_data['blog_content']
#         description = form.cleaned_data['description']
#         blog_img = form.cleaned_data['blog_img']
#         create_date = form.cleaned_data['create_date']
#         Blog.objects.create(title=title, content=content, description=description,blog_img=blog_img, create_date=create_date)
#         if form.is_valid():
#             form.save()
#             return redirect('add_blog')
#     else:
#         return render(request, 'blog_app/create_blog.html')

